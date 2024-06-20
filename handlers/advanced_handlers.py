import os
from json import dumps, loads

from gtts import gTTS
from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

import scripts.message_text as message_text
from database.database_manager import get_row, insert_into_db
from database.sql_query import (
    INSERT_GPT_ANSWER_JSON,
    INSERT_TOTAL_TOKENS,
    SELECT_CONTEXT,
    SELECT_COUNT_ANSWERS,
)
from handlers.button import selected_voice
from scripts.utils import logger_init
from service.tts import text_to_speech
from service.whisper import preprocess_audio
from service.yandex_gpt import _get_response_yandex_gpt

logger = logger_init("log.log")
user_states = {}


async def voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_states[user_id] = True
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=message_text.VOICE_START
    )


async def voice_message(update: Update, context: CallbackContext):
    id = update.message.from_user["id"]
    logger.info(f"Processing message from user {id}")
    if user_states.get(id, False):
        logger.info(f"Getting context for {id}")
        context_message = await get_row(SELECT_CONTEXT.format(telegram_id=id))
        if context_message is None:
            context_message = []
        else:
            try:
                context_message = loads(context_message["context"])
                logger.info(f"Loaded context for {id}: {context_message}")
            except Exception as e:
                logger.error(f"Error loading context for {id}: {e}")
                context_message = []
        logger.info(f"Getting voice message for {id}")
        voice = update.message.voice
        file_id = voice.file_id
        logger.info(f"Voice message file id for {id}: {file_id}")

        new_file = await context.bot.get_file(file_id)
        file_path = os.path.join("downloads", f"{file_id}.ogg")
        await new_file.download_to_drive(file_path)
        text = preprocess_audio(file_path)
        context_message.append({"role": "user", "text": text})
        gpt_answer, total_tokens = _get_response_yandex_gpt(context_message, text)
        context_message.append({"role": "assistant", "text": gpt_answer})
        if selected_voice.get(id, "2") == "2":
            tts = gTTS(text=gpt_answer, lang="ru")
            tts.save("voice_clone/outputs/voice.ogg")
            with open("voice_clone/outputs/voice.ogg", "rb") as audio:
                await context.bot.send_voice(
                    chat_id=update.effective_chat.id, voice=audio
                )
        else:
            text_to_speech(text=gpt_answer)
            with open("voice_clone/outputs/output.ogg", "rb") as audio:
                await context.bot.send_voice(
                    chat_id=update.effective_chat.id, voice=audio
                )

        await insert_into_db(
            INSERT_GPT_ANSWER_JSON.format(
                id=id,
                context=dumps(context_message, ensure_ascii=False),
                gpt_answer=gpt_answer,
            )
        )
        counts = await get_row(SELECT_COUNT_ANSWERS.format(telegram_id=id))
        if counts is None:
            count_answers = 1
            count_tokens = int(total_tokens)
        else:
            count_answers = int(counts["count_answers"]) + 1
            count_tokens = int(counts["tokens_output"]) + int(total_tokens)
        cost = round(count_tokens * 0.0002, 5)
        await insert_into_db(
            INSERT_TOTAL_TOKENS.format(
                telegram_id=id, count=count_answers, tokens=count_tokens, cost=cost
            )
        )
    else:
        await update.message.reply_text("Пожалуйста, сначала введите команду /voice.")
    # await update.message.reply_text(f'{answer_gpt}')

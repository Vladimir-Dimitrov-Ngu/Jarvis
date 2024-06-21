from telegram import Update
from telegram.ext import ContextTypes

import scripts.message_text as message_text
from database.database_manager import get_row, insert_into_db
from database.sql_query import DELETE_CONTEXT, SELECT_COUNT_ANSWERS
from handlers.voice_handler import user_states


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=message_text.START
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=message_text.HELP
    )


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_states[user_id] = False
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Вы вышли из голосового режима"
    )


async def clear_context(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    await insert_into_db(DELETE_CONTEXT.format(id=user_id))
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Ваш контекст очищен"
    )


async def analytics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id = update.message.from_user.id
    counts = await get_row(SELECT_COUNT_ANSWERS.format(telegram_id=id))
    if counts is None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Вы еще не общались с ботом"
        )
    else:
        tokens, count, cost, toxic_rating = (
            counts["tokens_output"],
            counts["count_answers"],
            round(counts["cost"], 3),
            counts["toxic_rating"],
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Количество использованных токенов: {tokens}\nКоличество обращений: {count}\nПотрачено рублей: {cost}\nКоличество токсичных сообщений: {toxic_rating}",
        )


async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Ваш контекст очищен"
    )

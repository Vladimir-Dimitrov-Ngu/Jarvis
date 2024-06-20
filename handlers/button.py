from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

selected_voice = {}
answers = {"1": "Мужчина", "2": "Женщина"}


async def voice_choose(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Мужчина", callback_data="1"),
            InlineKeyboardButton("Женщина", callback_data="2"),
        ],
        # [InlineKeyboardButton("Option 3", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Кто с вами будет разговаривать", reply_markup=reply_markup
    )


# Функция для обработки нажатий на кнопки
async def voice_button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id
    query.answer()
    await query.edit_message_text(text=f"Вы выбрали: {answers[query.data]}")
    selected_voice[user_id] = query.data


# def error(update: Update, context: CallbackContext) -> None:
#     """Log Errors caused by Updates."""
#     logger.warning('Update "%s" caused error "%s"', update, context.error)

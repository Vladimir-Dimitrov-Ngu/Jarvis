import time

from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler,
                          filters, CallbackQueryHandler)

import config
from handlers.common_handlers import cancel, help, start, clear_context, analytics
from handlers.advanced_handlers import voice, voice_message, logger
from handlers.button import voice_choose, voice_button


COMMAND_HANDLERS = {
    "start": start,
    "help": help,
    "cancel": cancel,
    "voice":voice,
    "clear": clear_context,
    "analytics": analytics,
    "voice_choose": voice_choose,
}

if __name__ == "__main__":
    start_time = time.time()
    application = ApplicationBuilder().token(config.API_TOKEN).build()

    for command_name, command_handler in COMMAND_HANDLERS.items():
        application.add_handler(CommandHandler(command_name, command_handler))

    application.add_handler(
        MessageHandler(filters.VOICE & ~filters.COMMAND, voice_message)
    )
    application.add_handler(CallbackQueryHandler(voice_button))

    time_to_start = round(time.time() - start_time, 2)
    logger.info(f'It took {time_to_start} to start the application')
    application.run_polling()

import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CommandHandler, ContextTypes, MessageHandler, filters, ApplicationBuilder
from dialogue import start_dialogue, handle_dialogue
from MessageLogger.message_logger import MessageLogger
import constants
from authorization import authorize, handle_authorization, check_authorization

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

storage = MessageLogger()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(constants.WELCOME_MESS)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if not await check_authorization(update, context):
        return

    await update.message.reply_text(constants.HELP_MESS)

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if not await check_authorization(update, context):
        return

    await update.message.reply_text(constants.UNKNOWN_MESS)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if 'mode' not in context.user_data:
        await update.message.reply_text(constants.MISS_MODE)
        return

    storage.add_record('user', update.message.text)

    mode = context.user_data['mode']

    if mode != 'authorization' and not await check_authorization(update, context):
        return

    match mode:
        case 'dialogue':
            await handle_dialogue(update, context)
        case 'authorization':
            await handle_authorization(update, context)

async def stop_mode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if not await check_authorization(update, context):
        return

    if 'mode' not in context.user_data:
        await update.message.reply_text(constants.MISS_MODE)
        return

    await update.message.reply_text(
        constants.STOP_MESS.format(context.user_data['mode']),
        reply_markup=ReplyKeyboardRemove()
    )
    context.user_data.pop('mode')
    context.user_data.pop('history')

def main():

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('info', info))
    app.add_handler(CommandHandler('dialogue', start_dialogue))
    app.add_handler(CommandHandler('stop', stop_mode))
    app.add_handler(CommandHandler('authorize', authorize))

    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))
    app.run_polling()

if __name__ == '__main__':
    main()
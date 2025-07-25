import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes
import constants

load_dotenv()
PASSWORD = os.getenv("PASSWORD")

async def authorize(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if 'activate' in context.user_data and context.user_data['activate']:
        await update.message.reply_text(constants.ALR_AUTH)
        return

    context.user_data['mode'] = 'authorization'

    await update.message.reply_text(constants.AUTH_ASK)

async def handle_authorization(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if update.message.text == PASSWORD:
        await update.message.reply_text(constants.COR_PASSW)
        await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=constants.STICKER_ID)
        context.user_data['activate'] = True
        context.user_data.pop('mode')
    else:
        await update.message.reply_text(constants.INCOR_PASSW)

async def check_authorization(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    if 'activate' in context.user_data and context.user_data['activate']:
        return True

    await update.message.reply_text(
        constants.MISS_AUTH,
        reply_markup=ReplyKeyboardRemove()
    )
    return False
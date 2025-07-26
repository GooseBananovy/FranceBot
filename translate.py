from telegram import Update
from telegram.ext import ContextTypes
import translate_setttings
from authorization import check_authorization
import constants

async def start_translate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if not await check_authorization(update, context):
        return

    context.user_data['flagTranslate'] = True

    await update.message.reply_text(constants.TRANS_MESS)


async def handle_translate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    text = update.message.text
    source = await guesslang(text)
    target = 'ru' if source == 'fr' else 'fr'
    result = await translate_setttings.translate(text, source, target)

    await update.message.reply_text(result)

async def translate_last(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if not await check_authorization(update, context):
        return

    if 'mode' not in context.user_data:
        await update.message.reply_text(constants.MISS_MODE)
        return

    if 'history' not in context.user_data:
        await update.message.reply_text(constants.UNKNOWN_ERR)
        return

    if context.user_data['history'][-1]['role'] == 'system' or context.user_data['history'][-1]['role'] == 'user':
        await update.message.reply_text(constants.MISS_MESS_FROM_BOT)
        return

    text = context.user_data['history'][-1]['content']
    source = await guesslang(text)
    target = 'ru' if source == 'fr' else 'fr'

    result = await translate_setttings.translate(text, source, target)

    await update.message.reply_text(result)


async def guesslang(text: str) -> str:
    #Returns 'ru' or 'fr'

    cnt_ru = 0
    total_cnt = 0

    for ch in text:
        if ch.isalpha():
            total_cnt += 1

            if ('А' <= ch <= 'Я') or ('а' <= ch <= 'я') or (ch == 'Ё') or (ch == 'ё'):
                cnt_ru += 1

    if not total_cnt:
        return 'ru'

    return 'ru' if cnt_ru / total_cnt >= 0.5 else 'fr'
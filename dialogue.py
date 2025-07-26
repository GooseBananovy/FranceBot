import constants
from ai_settings import get_ai_response
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from authorization import check_authorization

async def start_dialogue(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if not await check_authorization(update, context):
        return

    mode = 'dialogue'

    if 'mode' in context.user_data:
        await update.message.reply_text(
            constants.SWITCH_MESS.format(context.user_data['mode'], mode) if context.user_data['mode'] != mode
            else constants.RESET_MESS.format(mode)
        )

    context.user_data.update({
        'mode': mode,
        'history': [{'role': 'system', 'content': constants.DIALOGUE_PROMPT}],
    })

    await update.message.reply_text(
        constants.DIALOGUE_START_MESS,
        reply_markup=ReplyKeyboardMarkup(constants.DIAL_BUTTONS, resize_keyboard=True)
    )

async def handle_dialogue(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = {
        'role': 'user',
        'content': update.message.text
    }
    context.user_data['history'].append(user_message)

    response = await get_ai_response(messages=context.user_data['history'])
    if not response:
        await update.message.reply_text(constants.UNKNOWN_ERR)
        return

    model_message = {
        'role': 'assistant',
        'content': response
    }
    context.user_data['history'].append(model_message)

    await update.message.reply_text(response)


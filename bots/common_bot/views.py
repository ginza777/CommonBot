from telegram import Update
from telegram.ext import CallbackContext

from .main_bot.models import User
from .default_handlers.check_subscription.handlers import add_ask_subscribe_channel
from .default_handlers.language.handlers import ask_language
from .default_handlers.onboarding import static_text
from .default_handlers.onboarding.keyboards import make_keyboard_for_start_command
from .main_bot.bot import Bot_settings


@add_ask_subscribe_channel
def start(update: Update, context: CallbackContext, subscribe: bool) -> None:
    u, created = User.get_user_and_created(update, context)
    if created:
        text = static_text.start_created.format(first_name=u.first_name)
    else:
        text = static_text.start_not_created.format(first_name=u.first_name)

    if Bot_settings.force_language:
        ask_language(update, context)

    if subscribe:
        update.message.reply_text(text=text,
                                  reply_markup=make_keyboard_for_start_command())

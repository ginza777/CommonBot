"""
    Telegram event handlers
"""
from django.conf import settings
from telegram import Bot
from telegram.ext import (
    Dispatcher, CommandHandler, MessageHandler, CallbackQueryHandler, Filters, )

from . import views
from .default_handlers.admin import handlers as admin_handlers
from .default_handlers.broadcast_message import handlers as broadcast_handlers
from .default_handlers.broadcast_message.handlers import broadcast_command
from .default_handlers.broadcast_message.manage_data import CONFIRM_DECLINE_BROADCAST
from .default_handlers.check_subscription import handlers as check_subscription_handlers
from .default_handlers.language import handlers as language_handlers
from .default_handlers.location import handlers as location_handlers
from .default_handlers.onboarding import handlers as onboarding_handlers
from .default_handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON
from .main_bot.bot import Bot_settings


def setup_dispatcher(dp):
    dp.add_handler(MessageHandler(Filters.update.channel_posts, onboarding_handlers.ignore_updates))
    dp.add_handler(MessageHandler(Filters.group, onboarding_handlers.ignore_updates))
    """
    Adding handlers for events from Telegram
    """
    dp.add_handler(CommandHandler("start", views.start))

    # location
    dp.add_handler(CommandHandler("ask_location", location_handlers.ask_for_location))
    dp.add_handler(MessageHandler(Filters.location, location_handlers.location_handler))

    # admin commands
    dp.add_handler(CommandHandler("admin", admin_handlers.admin))
    dp.add_handler(CommandHandler("stats", admin_handlers.stats))
    dp.add_handler(CommandHandler("backup_db", admin_handlers.backup_db))
    dp.add_handler(CommandHandler('export_users', admin_handlers.export_users))
    dp.add_handler(
        MessageHandler(Filters.regex(rf'^{broadcast_command}(/s)?.*'),
                       broadcast_handlers.broadcast_command_with_message)
    )
    # secret level
    dp.add_handler(CallbackQueryHandler(onboarding_handlers.secret_level, pattern=f"^{SECRET_LEVEL_BUTTON}"))

    dp.add_handler(
        CallbackQueryHandler(broadcast_handlers.broadcast_decision_handler, pattern=f"^{CONFIRM_DECLINE_BROADCAST}")
    )

    # about help
    dp.add_handler(CommandHandler("help", onboarding_handlers.help))
    dp.add_handler(CommandHandler("about", onboarding_handlers.about))
    dp.add_handler(CommandHandler("language", language_handlers.ask_language))

    # check subscription
    dp.add_handler(
        CallbackQueryHandler(check_subscription_handlers.check_subscription_channel, pattern="^check_subscription"))

    # choice language
    dp.add_handler(CallbackQueryHandler(language_handlers.language_choice_handle, pattern="^language_setting_"))

    return dp


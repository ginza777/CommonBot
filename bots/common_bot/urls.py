from .main_bot.urls import *  # noqa   import urlpatterns
from .api import UserApi,LocationApi,ChannelApi
from .apps import BotConfig
from django.urls import path

urlpatterns+=[
    path(f'api/v1/bot/{BotConfig.app_url}/user/', UserApi.as_view(), name='user_to_json'),
    path(f'api/v1/bot/{BotConfig.app_url}/location/', LocationApi.as_view(), name='location_to_json'),
    path(f'api/v1/bot/{BotConfig.app_url}/channel/', ChannelApi.as_view(), name='channel_to_json'),
]
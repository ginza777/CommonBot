from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .apps import BotConfig
from .models import User, Location, Channel

app_name = BotConfig.app_url


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        ref_name = f"{app_name}_user"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        ref_name = f"{app_name}_location"


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'
        ref_name = f"{app_name}_channel"


class UserApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ChannelApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

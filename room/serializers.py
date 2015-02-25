from .models import Room
from rest_framework import serializers


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'name'
        ]


class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'name',
            'floor'
        ]

from .models import Room
from rest_framework import serializers


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'name',
            'capacity',
            'building_name',
            'floor'
        ]


class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'name',
            'capacity',
            'building_name',
            'floor',
            'available_since',
            'has_speakers',
            'has_projector',
            'has_black_board'
        ]

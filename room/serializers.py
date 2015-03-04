from .models import Room
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoModelSerializer


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'name',
            'capacity',
            'building_name',
            'floor'
        ]


class RoomDetailSerializer(GeoModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'name',
            'capacity',
            'building_name',
            'floor',
            'available_since',
            'position',
            'has_speakers',
            'has_projector',
            'has_black_board',
        ]

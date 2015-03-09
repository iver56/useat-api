from .models import Room
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoModelSerializer
from rest_framework.serializers import SerializerMethodField


class RoomListSerializer(GeoModelSerializer):
    distance = SerializerMethodField()

    class Meta:
        model = Room
        fields = [
            'id',
            'name',
            'capacity',
            'building_name',
            'floor',
            'distance'
        ]

    def get_distance(self, room):
        if hasattr(room, 'distance') and room.distance is not None:
            return int(round(room.distance.m))
        return None


class RoomDetailSerializer(RoomListSerializer):
    class Meta(RoomListSerializer.Meta):
        fields = RoomListSerializer.Meta.fields + [
            'available_since',
            'position',
            'has_speakers',
            'has_projector',
            'has_black_board',
        ]

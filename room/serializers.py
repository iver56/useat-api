from .models import Room
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoModelSerializer
from rest_framework.serializers import SerializerMethodField
from room_feature.serializers import RoomFeatureListSerializer


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
    features = RoomFeatureListSerializer(many=True)

    class Meta(RoomListSerializer.Meta):
        fields = RoomListSerializer.Meta.fields + [
            'available_since',
            'position',
            'features',
        ]

from .models import RoomFeature
from rest_framework.serializers import ModelSerializer


class RoomFeatureListSerializer(ModelSerializer):
    class Meta:
        model = RoomFeature
        fields = [
            'id',
            'name'
        ]

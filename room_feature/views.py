from .models import RoomFeature
from rest_framework import viewsets
from .serializers import RoomFeatureListSerializer


class RoomFeatureViewSet(viewsets.ModelViewSet):
    queryset = RoomFeature.objects.all()
    serializer_class = RoomFeatureListSerializer

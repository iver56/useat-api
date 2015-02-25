from .models import Room
from rest_framework import viewsets
from .serializers import RoomDetailSerializer, RoomListSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RoomDetailSerializer
        return RoomListSerializer

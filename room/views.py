from .models import Room
from rest_framework import viewsets
from .serializers import RoomDetailSerializer, RoomListSerializer
from rest_framework.decorators import detail_route
from django.core.exceptions import PermissionDenied
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from django.utils import timezone


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RoomDetailSerializer
        return RoomListSerializer

    @detail_route(methods=['post'])
    def report_availability(self, request, pk=None):
        room = self.get_object()
        try:
            is_available = int(request.DATA['is_available'])
        except:
            raise ParseError(detail="Must specify is_available that is an integer")

        if is_available < 0:
            raise ParseError(detail="is_available must be non-negative")

        if is_available:
            room.available_since = timezone.now()
        else:
            room.available_since = None
        room.save()

        return Response({'status': 'ok'})

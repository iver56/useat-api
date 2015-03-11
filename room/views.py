from .models import Room
from rest_framework import viewsets
from .serializers import RoomDetailSerializer, RoomListSerializer
from rest_framework.decorators import detail_route, list_route
from django.core.exceptions import PermissionDenied
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from django.utils import timezone
from hub.models import Hub
from django.contrib.gis.geos import Point


class RoomViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RoomDetailSerializer
        return RoomListSerializer

    def get_queryset(self):
        queryset = Room.objects.all()
        if self.action not in {'retrieve', 'list', 'favorites'}:
            return queryset

        lat = self.request.QUERY_PARAMS.get('lat', None)
        lon = self.request.QUERY_PARAMS.get('lon', None)

        if lat is None or lon is None:
            raise ParseError(detail="lat and lon are required query params")

        try:
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            raise ParseError(detail="lat or lon is not float")

        ref_location = Point(lon, lat)

        if self.action == 'list':
            queryset = queryset.filter(available_since__isnull=False)

        return queryset.distance(ref_location).order_by('distance')

    @detail_route(methods=['post'])
    def report_availability(self, request, pk=None):
        room = self.get_object()

        try:
            hub_token = request.DATA['hub_token']
        except:
            raise ParseError(detail='hub_token must be specified')

        try:
            hub = Hub.objects.get(token=hub_token)
        except Hub.DoesNotExist:
            raise PermissionDenied()

        if not hub.room_permissions.filter(id=room.id).exists():
            raise PermissionDenied()

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

        room.last_sensor_reading_time = timezone.now()

        room.save()

        return Response({'status': 'ok'})

    @list_route()
    def favorites(self, request):
        ids = self.request.QUERY_PARAMS.get('ids', None)
        if ids is None:
            raise ParseError(detail="ids required")
        ids = ids.split(',')

        queryset = self.get_queryset().filter(id__in=ids)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

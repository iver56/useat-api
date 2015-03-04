from django.contrib.gis import admin
from .models import Room


class RoomAdmin(admin.OSMGeoAdmin):
    default_lon = 1157108.48900
    default_lat = 9205549.12020
    default_zoom = 12


admin.site.register(Room, RoomAdmin)

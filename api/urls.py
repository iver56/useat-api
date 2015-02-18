from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from room import views as room_views

router = routers.DefaultRouter()
router.register(r'rooms', room_views.RoomViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]

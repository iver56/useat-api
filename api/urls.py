from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework import routers
from room import views as room_views
from room_feature import views as room_feature_views

router = routers.DefaultRouter()
router.register(r'rooms', room_views.RoomViewSet, base_name='rooms')
router.register(r'room_features', room_feature_views.RoomFeatureViewSet, base_name='room_features')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

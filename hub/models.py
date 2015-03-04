from django.db import models
from room.models import Room
from django.utils.encoding import smart_unicode


class Hub(models.Model):
    name = models.CharField(max_length=20, help_text="Human-readable identifier")
    token = models.CharField(max_length=40, null=False)
    room_permissions = models.ManyToManyField(Room, related_name='hubs')

    def __unicode__(self):
        return smart_unicode(
            "Hub " + self.name
        )

from django.db import models
from django.utils.encoding import smart_unicode


class RoomFeature(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __unicode__(self):
        return smart_unicode(self.name)

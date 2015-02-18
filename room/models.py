from django.db import models
from django.utils.encoding import smart_unicode


class Room(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    floor = models.IntegerField(null=True,
                                blank=True,
                                help_text='0 (zero) represents the ground floor')

    def __unicode__(self):
        return smart_unicode(
            "Room " + self.name + ", floor: " + str(self.floor)
        )

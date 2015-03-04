from django.db import models
from django.utils.encoding import smart_unicode


class Room(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    floor = models.IntegerField(null=True,
                                blank=True,
                                help_text='0 (zero) represents the ground floor')
    building_name = models.CharField(max_length=50, null=True, blank=True)
    capacity = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="How many persons is the room intended for?"
    )
    available_since = models.DateTimeField(null=True,
                                           blank=True,
                                           help_text="Is NULL when the room is occupied")
    last_sensor_reading_time = models.DateTimeField(null=True, blank=True)

    # Features
    has_speakers = models.BooleanField(default=False)
    has_projector = models.BooleanField(default=False)
    has_black_board = models.BooleanField(default=False)

    def __unicode__(self):
        return smart_unicode(
            "Room " + self.name + ", floor: " + str(self.floor)
        )

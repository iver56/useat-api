# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_room_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='has_black_board',
        ),
        migrations.RemoveField(
            model_name='room',
            name='has_projector',
        ),
        migrations.RemoveField(
            model_name='room',
            name='has_speakers',
        ),
    ]

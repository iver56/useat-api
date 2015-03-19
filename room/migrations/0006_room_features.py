# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_feature', '0001_initial'),
        ('room', '0005_room_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='features',
            field=models.ManyToManyField(to='room_feature.RoomFeature'),
            preserve_default=True,
        ),
    ]

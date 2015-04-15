# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_room_mazemap_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='features',
            field=models.ManyToManyField(to='room_feature.RoomFeature', blank=True),
            preserve_default=True,
        ),
    ]

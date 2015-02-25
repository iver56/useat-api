# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_auto_20150225_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='last_sensor_reading_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='available_since',
            field=models.DateTimeField(help_text=b'Is NULL when the room is occupied', null=True, blank=True),
            preserve_default=True,
        ),
    ]

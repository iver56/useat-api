# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_auto_20150218_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='available_since',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='building_name',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.PositiveIntegerField(help_text=b'How many persons is the room intended for?', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='has_black_board',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='has_projector',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='has_speakers',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

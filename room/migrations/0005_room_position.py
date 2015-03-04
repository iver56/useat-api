# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import room.models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_auto_20150225_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='position',
            field=django.contrib.gis.db.models.fields.PointField(default=room.models.default_point, srid=4326),
            preserve_default=True,
        ),
    ]

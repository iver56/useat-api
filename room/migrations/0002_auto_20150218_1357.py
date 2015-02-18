# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='floor',
            field=models.IntegerField(help_text=b'0 (zero) represents the ground floor', null=True, blank=True),
            preserve_default=True,
        ),
    ]

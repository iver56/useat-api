# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0007_auto_20150319_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='mazemap_url',
            field=models.CharField(help_text=b'Url for embedding mazemap', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_auto_20150225_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Human-readable identifier', max_length=20)),
                ('token', models.CharField(max_length=40)),
                ('room_permissions', models.ManyToManyField(related_name='hubs', to='room.Room')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-21 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0018_askaquestion_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='askaquestion',
            old_name='delete',
            new_name='can_delete',
        ),
        migrations.AddField(
            model_name='askaquestion',
            name='can_update',
            field=models.BooleanField(default=False),
        ),
    ]

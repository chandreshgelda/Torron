# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-25 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0041_auto_20180725_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='likes_comment',
        ),
        migrations.AddField(
            model_name='comments',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]

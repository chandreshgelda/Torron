# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-30 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0010_auto_20180530_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='user',
        ),
        migrations.AddField(
            model_name='report',
            name='username',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
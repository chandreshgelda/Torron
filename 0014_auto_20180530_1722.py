# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-30 17:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0013_auto_20180530_1704'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='hidden_post',
            new_name='hidden',
        ),
    ]

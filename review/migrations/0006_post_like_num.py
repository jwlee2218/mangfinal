# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_auto_20170809_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_num',
            field=models.IntegerField(default=0),
        ),
    ]

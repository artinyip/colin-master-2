# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-15 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0006_auto_20160908_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_added'),
        ),
    ]

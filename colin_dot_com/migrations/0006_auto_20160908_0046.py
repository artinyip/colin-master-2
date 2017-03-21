# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-08 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0005_auto_20160908_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='tag',
            field=models.ManyToManyField(blank=True, to='colin_dot_com.PhotoTag'),
        ),
    ]
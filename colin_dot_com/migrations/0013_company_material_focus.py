# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-28 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0012_auto_20160924_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='material_focus',
            field=models.CharField(choices=[('WOD', 'Wood'), ('MTL', 'Metal'), ('GLA', 'Glass'), ('PRT', 'Print'), ('CER', 'Ceramic'), ('TEX', 'Textile'), ('ADV', 'Advanced Manufacturing')], default='N/A', max_length=3, verbose_name='Material Focus'),
        ),
    ]
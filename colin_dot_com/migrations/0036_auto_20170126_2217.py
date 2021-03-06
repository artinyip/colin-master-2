# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-27 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0035_auto_20170114_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='designer',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='designer',
            name='interest',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('WOD', 'Wood'), ('MTL', 'Metal'), ('GLA', 'Glass'), ('PRT', 'Print'), ('CER', 'Ceramic'), ('TEX', 'Textile'), ('ADV', 'Advanced Manufacturing'), ('OTH', 'Other')], default='N/A', max_length=31, verbose_name='Material Focus'),
        ),
    ]

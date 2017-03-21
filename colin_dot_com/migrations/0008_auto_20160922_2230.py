# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-23 02:30
from __future__ import unicode_literals

import address.models
from django.db import migrations
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('colin_dot_com', '0007_auto_20160915_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=address.models.AddressField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='address.Address'),
        ),
        migrations.AddField(
            model_name='company',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
    ]
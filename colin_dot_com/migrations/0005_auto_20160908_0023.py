# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-08 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0004_company_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='tag',
            field=models.ManyToManyField(to='colin_dot_com.PhotoTag'),
        ),
    ]

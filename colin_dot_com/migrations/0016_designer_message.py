# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-13 00:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('colin_dot_com', '0015_auto_20161008_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, default='', max_length=1000)),
                ('body', models.TextField(default='')),
                ('date_sent', models.DateField(auto_now_add=True)),
                ('date_read', models.DateField(blank=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Recipient', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

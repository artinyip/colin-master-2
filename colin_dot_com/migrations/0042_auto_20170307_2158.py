# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0041_auto_20170307_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(blank=True, null=True, max_length=500)),
                ('body', models.TextField()),
                ('featured_image', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='post',
            field=models.ForeignKey(to='colin_dot_com.Post', related_name='gallery'),
        ),
    ]

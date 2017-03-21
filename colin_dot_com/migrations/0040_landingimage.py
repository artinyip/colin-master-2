# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0039_auto_20170307_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.CharField(max_length=300)),
                ('company', models.ForeignKey(to='colin_dot_com.Company', related_name='company', null=True)),
            ],
        ),
    ]

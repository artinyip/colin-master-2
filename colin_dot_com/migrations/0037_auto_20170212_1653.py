# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0036_auto_20170126_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='designer',
            name='firm',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='designer',
            name='position',
            field=models.TextField(default='', max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0037_auto_20170212_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='designer',
            name='city',
            field=models.CharField(max_length=1000, default=''),
        ),
        migrations.AddField(
            model_name='designer',
            name='state',
            field=models.CharField(max_length=2, default=''),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0029_auto_20161208_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='blurb',
            field=models.TextField(max_length=400, default=''),
        ),
    ]

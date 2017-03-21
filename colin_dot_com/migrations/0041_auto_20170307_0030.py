# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0040_landingimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingimage',
            name='company',
            field=models.ForeignKey(null=True, to='colin_dot_com.Company', related_name='company', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0027_auto_20161017_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='material_focus',
            field=models.CharField(verbose_name='Material Focus', max_length=3, default='N/A', choices=[('WOD', 'Wood'), ('MTL', 'Metal'), ('GLA', 'Glass'), ('PRT', 'Print'), ('CER', 'Ceramic'), ('TEX', 'Textile'), ('ADV', 'Advanced Manufacturing'), ('OTH', 'Other')]),
        ),
    ]

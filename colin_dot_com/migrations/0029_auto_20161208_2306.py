# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0028_auto_20161119_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='material',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='material',
        ),
        migrations.RemoveField(
            model_name='product',
            name='short_size',
        ),
        migrations.AlterField(
            model_name='company',
            name='blurb',
            field=models.TextField(default='', max_length=350),
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Designer',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='MaterialTag',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ShortSize',
        ),
    ]

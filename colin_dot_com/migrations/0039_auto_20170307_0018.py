# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0038_auto_20170212_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageattachment',
            name='message',
            field=models.ForeignKey(null=True, related_name='attachments', to='colin_dot_com.Message'),
        ),
    ]

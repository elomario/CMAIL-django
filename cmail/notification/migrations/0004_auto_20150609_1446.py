# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_auto_20150609_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='photo',
            field=models.ForeignKey(to='photo.Photo', null=True),
        ),
    ]

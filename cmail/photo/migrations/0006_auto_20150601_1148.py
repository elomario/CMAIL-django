# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_auto_20150601_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.OneToOneField(to='photo.Photo'),
        ),
    ]

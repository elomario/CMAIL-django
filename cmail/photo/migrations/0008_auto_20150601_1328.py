# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0007_auto_20150601_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='photo',
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='static', blank=True),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_notification_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='photo',
            field=models.OneToOneField(null=True, to='photo.Photo'),
        ),
    ]

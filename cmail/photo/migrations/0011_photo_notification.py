# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0005_remove_notification_photo'),
        ('photo', '0010_remove_photo_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='notification',
            field=models.ForeignKey(null=True, to='notification.Notification'),
        ),
    ]

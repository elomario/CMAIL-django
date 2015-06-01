# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
        ('photo', '0008_auto_20150601_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='notification',
            field=models.ForeignKey(null=True, to='notification.Notification'),
        ),
    ]

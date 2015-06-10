# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0005_remove_notification_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='checked',
            field=models.CharField(max_length=6, default='false', choices=[('true', 'true'), ('false', 'false')]),
        ),
    ]

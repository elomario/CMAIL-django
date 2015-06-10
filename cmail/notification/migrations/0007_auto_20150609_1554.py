# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0006_notification_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='checked',
            field=models.IntegerField(default='1', choices=[('0', 'true'), ('1', 'false')]),
        ),
    ]

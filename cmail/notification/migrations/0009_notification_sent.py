# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0008_auto_20150609_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='sent',
            field=models.IntegerField(default='1'),
        ),
    ]

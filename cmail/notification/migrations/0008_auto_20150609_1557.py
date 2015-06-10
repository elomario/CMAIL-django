# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0007_auto_20150609_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='checked',
            field=models.IntegerField(choices=[(0, 'true'), (1, 'false')], default='1'),
        ),
    ]

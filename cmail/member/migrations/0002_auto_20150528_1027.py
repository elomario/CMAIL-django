# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='billingaddress',
            field=models.CharField(max_length=45, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='surname',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]

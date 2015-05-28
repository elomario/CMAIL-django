# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='publication_date',
            field=models.DateTimeField(verbose_name='published on:', default=datetime.datetime(2015, 5, 28, 8, 17, 20, 579194, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]

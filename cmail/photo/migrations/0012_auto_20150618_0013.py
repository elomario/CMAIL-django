# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0011_photo_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='phototype',
            field=models.CharField(blank=True, max_length=9, choices=[('colis', 'colis'), ('enveloppe', 'enveloppe'), ('pub', 'pub'), ('suppose', 'suppose')]),
        ),
    ]

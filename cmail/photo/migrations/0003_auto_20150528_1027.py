# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_photo_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phototype',
            name='phototype',
            field=models.CharField(choices=[('colis', 'colis'), ('enveloppe', 'enveloppe'), ('pub', 'pub'), ('bordereau', 'bordereau')], max_length=9),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20150528_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='phototype',
            field=models.CharField(choices=[('colis', 'colis'), ('enveloppe', 'enveloppe'), ('pub', 'pub'), ('bordereau', 'bordereau')], max_length=9),
        ),
        migrations.DeleteModel(
            name='Phototype',
        ),
    ]

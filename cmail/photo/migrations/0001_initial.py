# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('image', models.ImageField(upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='Phototype',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('phototype', models.CharField(max_length=9, choices=[(1, 'colis'), (2, 'enveloppe'), (3, 'pub'), (4, 'bordereau')], blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='phototype',
            field=models.ForeignKey(to='photo.Phototype'),
        ),
    ]

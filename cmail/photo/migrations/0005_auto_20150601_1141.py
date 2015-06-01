# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20150528_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static')),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='image',
        ),
        migrations.AlterField(
            model_name='photo',
            name='phototype',
            field=models.CharField(max_length=9, choices=[('colis', 'colis'), ('enveloppe', 'enveloppe'), ('pub', 'pub'), ('bordereau', 'bordereau')], blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='photo',
            field=models.ForeignKey(to='photo.Photo'),
        ),
    ]

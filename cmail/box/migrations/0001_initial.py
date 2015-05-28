# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=45)),
                ('member', models.ManyToManyField(to='member.Member')),
                ('sim', models.ForeignKey(to='sim.Sim')),
            ],
        ),
    ]

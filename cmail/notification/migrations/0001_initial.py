# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=45)),
                ('description', models.CharField(blank=True, max_length=45)),
                ('box', models.ForeignKey(to='box.Box')),
            ],
        ),
    ]

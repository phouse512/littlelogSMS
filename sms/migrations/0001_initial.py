# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LittleLogAlias',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('alias', models.CharField(max_length=20)),
                ('email_secret', models.CharField(max_length=100)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='LittleLogHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('sent_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('log_text', models.CharField(max_length=255)),
                ('alias', models.ForeignKey(to='sms.LittleLogAlias')),
            ],
        ),
    ]

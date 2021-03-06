# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-17 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_jobposting_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='attended_event',
            field=models.ForeignKey(default=1, help_text='Event attended when this record was created or last updated.', on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
            preserve_default=False,
        ),
    ]

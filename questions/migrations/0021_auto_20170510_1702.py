# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0020_auto_20170510_0721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['-answer_date']},
        ),
        migrations.AddField(
            model_name='topic',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0024_auto_20170510_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='description',
            field=models.CharField(default=b'Description', max_length=100),
        ),
    ]

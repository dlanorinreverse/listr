# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_auto_20170507_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='details',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='details',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

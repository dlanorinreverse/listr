# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_auto_20170509_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
    ]

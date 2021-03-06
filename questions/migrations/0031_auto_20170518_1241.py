# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-18 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0030_auto_20170517_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='image',
            field=models.FileField(blank=True, upload_to=b'./storage/instructions/'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.FileField(blank=True, upload_to=b'./storage/topics/'),
        ),
    ]

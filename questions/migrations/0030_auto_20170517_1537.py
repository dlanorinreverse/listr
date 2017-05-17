# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import questions.models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0029_topic_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.FileField(blank=True, upload_to=questions.models.topic_image_uploadpath),
        ),
    ]

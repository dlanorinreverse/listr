# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0015_remove_person_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='downvotes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='upvotes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='downvotes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='upvotes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

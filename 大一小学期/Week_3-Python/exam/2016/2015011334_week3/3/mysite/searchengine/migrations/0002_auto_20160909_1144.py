# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ttime',
            field=models.CharField(max_length=200),
        ),
    ]

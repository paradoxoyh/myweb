# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-18 12:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0004_y'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='y',
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Y',
        ),
    ]
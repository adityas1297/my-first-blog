# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-19 13:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_data',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='test',
            new_name='text',
        ),
    ]

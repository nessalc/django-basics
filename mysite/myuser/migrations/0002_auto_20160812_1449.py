# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 19:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='identifier',
            new_name='email',
        ),
    ]

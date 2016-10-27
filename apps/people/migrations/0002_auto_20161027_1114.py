# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='landline',
            field=models.CharField(default=None, max_length=32, verbose_name='landline'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='mobile',
            field=models.CharField(default=1, max_length=32, verbose_name='mobile'),
            preserve_default=False,
        ),
    ]

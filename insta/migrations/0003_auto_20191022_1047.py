# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-22 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20191022_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comment',
            field=models.CharField(max_length=80, null=True),
        ),
    ]

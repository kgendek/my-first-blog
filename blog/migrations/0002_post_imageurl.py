# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-28 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imageurl',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_advisor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
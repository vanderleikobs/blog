# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 00:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visualizcoes',
            field=models.IntegerField(default=0),
        ),
    ]

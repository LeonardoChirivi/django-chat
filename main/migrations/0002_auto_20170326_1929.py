# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-26 17:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelTable(
            name='message',
            table='messages',
        ),
    ]

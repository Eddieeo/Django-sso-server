# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-19 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cas', '0003_options_sys_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='webs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]

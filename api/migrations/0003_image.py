# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_message_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]

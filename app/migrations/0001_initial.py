# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=255)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('positive', models.FloatField()),
                ('anger', models.FloatField()),
                ('sadness', models.FloatField()),
                ('disgust', models.FloatField()),
                ('percent_positive', models.FloatField()),
                ('percent_negative', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reviewer', models.CharField(max_length=100)),
                ('stars', models.FloatField()),
                ('comment', models.CharField(max_length=800, null=True)),
            ],
        ),
    ]
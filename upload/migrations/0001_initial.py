# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 03:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PIN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='pin',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.URL'),
        ),
    ]

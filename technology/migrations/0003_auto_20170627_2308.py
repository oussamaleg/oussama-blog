# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-27 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0002_auto_20170626_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='part',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='technology.Part'),
        ),
    ]

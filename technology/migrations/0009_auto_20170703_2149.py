# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-03 20:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('technology', '0008_blog_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birth', models.DateField()),
                ('photo', models.ImageField(upload_to='')),
                ('nabda', models.CharField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(verbose_name='تاريخ النشر'),
        ),
    ]

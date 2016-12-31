# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-17 18:13
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('points', '0003_point_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.DurationField()),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='points.Point')),
            ],
        ),
    ]
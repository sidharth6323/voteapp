# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-04 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='total_votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipebook', models.IntegerField(default=0)),
                ('signeasy', models.IntegerField(default=0)),
                ('helpchat', models.IntegerField(default=0)),
                ('volt', models.IntegerField(default=0)),
                ('strike', models.IntegerField(default=0)),
                ('buyhatke', models.IntegerField(default=0)),
                ('cleartax', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipebook', models.IntegerField(default=0)),
                ('signeasy', models.IntegerField(default=0)),
                ('helpchat', models.IntegerField(default=0)),
                ('volt', models.IntegerField(default=0)),
                ('strike', models.IntegerField(default=0)),
                ('buyhatke', models.IntegerField(default=0)),
                ('cleartax', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Poll.user')),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-21 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qrious', '0011_player_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_no', models.IntegerField(blank=True, default=1)),
                ('question_img', models.FileField(blank=True, upload_to='')),
                ('question', models.CharField(max_length=10000)),
                ('solution', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]
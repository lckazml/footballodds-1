# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-02-29 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_winalone_gameinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bigsmall',
            name='timeinterval',
        ),
        migrations.AddField(
            model_name='bigsmall',
            name='gameinfo',
            field=models.ForeignKey(blank=True, db_column='GameinfoId', default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Gameinfo'),
        ),
        migrations.AddField(
            model_name='letball',
            name='gameinfo',
            field=models.ForeignKey(blank=True, db_column='GameinfoId', default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Gameinfo'),
        ),
    ]

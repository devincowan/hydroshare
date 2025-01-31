# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-10-25 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs_access_control', '0034_auto_20211018_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupcommunityrequest',
            old_name='when_requested',
            new_name='when_community',
        ),
        migrations.RenameField(
            model_name='groupcommunityrequest',
            old_name='when_responded',
            new_name='when_group',
        ),
        migrations.AddField(
            model_name='community',
            name='closed',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]

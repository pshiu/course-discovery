# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-25 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0183_courserun_expected_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='MigrateCourseEditorsConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_keys', models.TextField(blank=True, default='', help_text='Comma separated organization keys e.g. edX, org2x,org3x,  org4x', verbose_name='Organization Keys')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

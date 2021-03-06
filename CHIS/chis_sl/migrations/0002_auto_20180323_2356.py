# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-23 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chis_sl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(blank=True, db_column='docEmail', max_length=100, null=True, verbose_name="doctor's email address"),
        ),
        migrations.AlterField(
            model_name='official',
            name='email',
            field=models.EmailField(blank=True, db_column='offEmail', max_length=100, null=True, verbose_name="official's email address"),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, db_column='patEmail', max_length=100, null=True, verbose_name="patient's email address"),
        ),
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.EmailField(blank=True, db_column='staEmail', max_length=100, null=True, verbose_name="staff's email address"),
        ),
    ]

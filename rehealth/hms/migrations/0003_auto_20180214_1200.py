# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-14 06:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0002_appointment_tips'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='doctor_id',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='patient_id',
            new_name='patient',
        ),
    ]
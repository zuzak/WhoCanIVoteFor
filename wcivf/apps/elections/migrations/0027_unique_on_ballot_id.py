# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-04 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("elections", "0026_postelection_voting_system")]

    operations = [
        migrations.AlterField(
            model_name="postelection",
            name="ballot_paper_id",
            field=models.CharField(blank=True, max_length=800, unique=True),
        )
    ]
# Generated by Django 3.1.1 on 2020-09-18 03:54

from django.db import migrations
import sortedm2m.fields
from sortedm2m.operations import *


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        AlterSortedManyToManyField(
            model_name='axe',
            name='strings',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='main_app.String'),
        ),
    ]

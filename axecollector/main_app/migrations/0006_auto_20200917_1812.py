# Generated by Django 3.1.1 on 2020-09-17 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_axe_strings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='string',
            old_name='name',
            new_name='line',
        ),
    ]
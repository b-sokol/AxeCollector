# Generated by Django 3.1.1 on 2020-09-17 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_string_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='axe',
            name='setup_specs',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]

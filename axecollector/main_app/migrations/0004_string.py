# Generated by Django 3.1.1 on 2020-09-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200916_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='String',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('guage', models.CharField(max_length=50)),
            ],
        ),
    ]

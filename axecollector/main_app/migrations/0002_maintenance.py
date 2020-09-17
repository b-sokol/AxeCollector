# Generated by Django 3.1.1 on 2020-09-16 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('service', models.CharField(choices=[('R', 'Restring'), ('S', 'Setup')], default='R', max_length=1)),
                ('axe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.axe')),
            ],
        ),
    ]
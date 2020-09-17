# Generated by Django 3.1.1 on 2020-09-16 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_maintenance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maintenance',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='maintenance',
            name='technician',
            field=models.CharField(default='Me', max_length=50),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='date',
            field=models.DateField(verbose_name='maintenance date'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='service',
            field=models.CharField(choices=[('R', 'Restring'), ('S', 'Setup'), ('E', 'Electronics'), ('C', 'Structural Repair'), ('F', 'Fretwork')], default='R', max_length=1),
        ),
    ]

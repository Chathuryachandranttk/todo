# Generated by Django 4.0.6 on 2022-07-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2022-07-22'),
            preserve_default=False,
        ),
    ]

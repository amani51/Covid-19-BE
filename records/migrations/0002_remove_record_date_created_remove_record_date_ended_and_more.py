# Generated by Django 4.1.7 on 2023-03-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='record',
            name='date_ended',
        ),
        migrations.AddField(
            model_name='record',
            name='date',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 4.2.9 on 2024-01-18 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='musician',
        ),
    ]

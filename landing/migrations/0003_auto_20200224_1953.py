# Generated by Django 3.0.3 on 2020-02-24 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_remove_sabscribers_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sabscribers',
            new_name='Sabscriber',
        ),
    ]

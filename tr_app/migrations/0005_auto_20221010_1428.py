# Generated by Django 3.2.16 on 2022-10-10 14:28

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('tr_app', '0004_rename_place_place_interest'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Place',
            new_name='Attraction',
        ),
        migrations.RenameModel(
            old_name='Interest',
            new_name='City',
        ),
    ]

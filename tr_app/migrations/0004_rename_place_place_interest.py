# Generated by Django 3.2.16 on 2022-10-05 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tr_app', '0003_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='place',
            new_name='interest',
        ),
    ]

# Generated by Django 3.2.16 on 2022-11-16 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tr_app', '0008_city_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='photo',
            field=models.ImageField(default='yet to be uploaded', upload_to='images/'),
            preserve_default=False,
        ),
    ]
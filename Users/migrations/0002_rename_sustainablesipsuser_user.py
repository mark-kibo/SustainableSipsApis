# Generated by Django 5.0 on 2023-12-22 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SustainableSipsUser',
            new_name='User',
        ),
    ]

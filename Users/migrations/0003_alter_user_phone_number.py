# Generated by Django 5.0 on 2023-12-28 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_rename_sustainablesipsuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
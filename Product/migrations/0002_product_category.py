# Generated by Django 5.0 on 2024-01-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='Alcohol', max_length=255),
        ),
    ]

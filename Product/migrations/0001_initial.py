# Generated by Django 5.0 on 2023-12-28 08:32
# Generated by Django 5.0 on 2023-12-25 12:24

import cloudinary.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='product_images')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('quantity', models.IntegerField(default=0)),
                ('buying_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

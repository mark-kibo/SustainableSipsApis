# Generated by Django 5.0 on 2023-12-25 09:43

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0007_delete_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sale_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales', to='Product.product')),
            ],
        ),
    ]

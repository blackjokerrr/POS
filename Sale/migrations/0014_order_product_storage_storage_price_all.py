# Generated by Django 3.0.3 on 2020-03-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sale', '0013_order_product_storage'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_product_storage',
            name='storage_price_all',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]

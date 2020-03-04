# Generated by Django 3.0.3 on 2020-03-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0010_auto_20200228_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]

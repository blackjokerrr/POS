# Generated by Django 3.0.3 on 2020-03-05 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0012_product_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.SmallIntegerField(max_length=3),
        ),
    ]
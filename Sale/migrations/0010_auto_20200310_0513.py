# Generated by Django 3.0.3 on 2020-03-09 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0029_auto_20200310_0447'),
        ('Sale', '0009_auto_20200310_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_product',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Management.Order'),
        ),
        migrations.AlterField(
            model_name='order_product',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Management.Product'),
        ),
    ]

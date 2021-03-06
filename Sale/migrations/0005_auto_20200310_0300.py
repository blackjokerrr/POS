# Generated by Django 3.0.3 on 2020-03-09 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0021_order_total_all'),
        ('Sale', '0004_save_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='save_product',
            name='order_all',
        ),
        migrations.AddField(
            model_name='save_product',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='Management.Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='save_product',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Management.Order'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-09 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0021_order_total_all'),
    ]

    operations = [
        migrations.CreateModel(
            name='Save_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Management.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Management.Product')),
            ],
        ),
    ]

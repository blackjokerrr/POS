# Generated by Django 3.0.3 on 2020-03-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0022_save_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='save_product',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]

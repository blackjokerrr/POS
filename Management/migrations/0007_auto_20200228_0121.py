# Generated by Django 3.0.3 on 2020-02-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0006_auto_20200228_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default=' ', max_length=200, null=True),
        ),
    ]

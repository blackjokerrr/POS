# Generated by Django 3.0.3 on 2020-02-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0005_auto_20200228_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
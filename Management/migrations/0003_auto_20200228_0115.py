# Generated by Django 3.0.3 on 2020-02-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0002_auto_20200227_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='description',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]

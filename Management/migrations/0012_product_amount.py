# Generated by Django 3.0.3 on 2020-03-05 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0011_auto_20200305_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.0.3 on 2020-03-05 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0017_auto_20200305_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='id_of_order',
            field=models.TextField(default=6262, max_length=6),
            preserve_default=False,
        ),
    ]

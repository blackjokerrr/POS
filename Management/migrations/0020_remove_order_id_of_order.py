# Generated by Django 3.0.3 on 2020-03-08 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0019_auto_20200306_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id_of_order',
        ),
    ]

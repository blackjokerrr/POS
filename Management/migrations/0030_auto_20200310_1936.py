# Generated by Django 3.0.3 on 2020-03-10 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0029_auto_20200310_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Management.Type'),
        ),
    ]

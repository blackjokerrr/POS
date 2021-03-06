# Generated by Django 3.0.3 on 2020-03-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('total_day', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('total_week', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('total_month', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('total_year', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
            ],
        ),
    ]

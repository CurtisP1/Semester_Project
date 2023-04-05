#  Copyright (c) 2023.

# Generated by Django 4.1.7 on 2023-03-25 20:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
                name='SineWaveData',
                fields=[
                    ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('data_val', models.DecimalField(decimal_places=20, max_digits=30)),
                    ('label', models.TimeField(auto_now=True)),
                ],
                options={
                    'db_table': 'dashboard_sinedata',
                    'managed' : False,
                },
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-01 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_sinedata_data_val'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sinedata',
            options={'ordering': ['-label']},
        ),
    ]

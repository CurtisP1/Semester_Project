# Generated by Django 4.1.7 on 2023-03-25 22:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='static/images/user_placeholder.png', upload_to='static/images/profile_pictures'),
        ),
    ]
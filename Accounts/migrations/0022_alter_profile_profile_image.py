# Generated by Django 4.1.5 on 2023-05-04 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0021_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/profpic.png', null=True, upload_to='images/'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-04-26 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0017_alter_post_post_image_alter_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=64, null=True),
        ),
    ]
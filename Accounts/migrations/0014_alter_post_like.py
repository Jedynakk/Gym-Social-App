# Generated by Django 4.1.5 on 2023-04-15 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0013_rename_user_post_author_post_date_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]

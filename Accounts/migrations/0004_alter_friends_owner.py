# Generated by Django 4.1.5 on 2023-03-15 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_remove_friends_owner_friends_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.profile'),
        ),
    ]

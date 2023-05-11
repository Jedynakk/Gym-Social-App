# Generated by Django 4.1.5 on 2023-03-15 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_alter_friends_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='friend',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='friend', to='Accounts.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='friends',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='Accounts.profile'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.5 on 2023-03-19 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_requestfriends_sent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestfriends',
            old_name='current_user',
            new_name='sender',
        ),
        migrations.RemoveField(
            model_name='requestfriends',
            name='friend',
        ),
        migrations.AddField(
            model_name='requestfriends',
            name='recipient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recipient', to='Accounts.profile'),
            preserve_default=False,
        ),
    ]

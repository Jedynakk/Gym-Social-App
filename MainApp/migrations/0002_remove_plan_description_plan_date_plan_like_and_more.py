# Generated by Django 4.1.5 on 2023-04-11 14:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0013_rename_user_post_author_post_date_post_like'),
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='description',
        ),
        migrations.AddField(
            model_name='plan',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='like',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='plan',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plan',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.profile'),
        ),
    ]
# Generated by Django 4.1.5 on 2023-04-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_remove_plan_description_plan_date_plan_like_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='description',
            field=models.TextField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
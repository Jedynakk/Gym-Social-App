# Generated by Django 4.1.5 on 2023-04-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_plan_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='description',
            field=models.TextField(max_length=256, null=True),
        ),
    ]
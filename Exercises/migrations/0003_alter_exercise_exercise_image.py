# Generated by Django 4.1.5 on 2023-05-07 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercises', '0002_exercise_exercise_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exercise_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

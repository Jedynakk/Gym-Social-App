# Generated by Django 4.1.5 on 2023-04-15 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exercises', '0001_initial'),
        ('Accounts', '0014_alter_post_like'),
        ('Plans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.PositiveIntegerField(default=0)),
                ('si', models.IntegerField(choices=[(1, 'KG'), (2, 'LBS'), (3, 'KM'), (4, 'MI')], default=1)),
                ('date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.profile')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exercises.exercise')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plans.plan')),
            ],
        ),
    ]

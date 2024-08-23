# Generated by Django 5.1 on 2024-08-23 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trainee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.IntegerField()),
                ('date', models.DateField()),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainee.trainee')),
            ],
        ),
    ]

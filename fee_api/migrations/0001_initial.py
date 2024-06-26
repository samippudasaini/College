# Generated by Django 4.2.8 on 2024-01-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10)),
                ('conform_password', models.CharField(max_length=10)),
                ('register_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

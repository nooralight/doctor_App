# Generated by Django 4.0.6 on 2022-12-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField(max_length=25)),
                ('doctor_name', models.TextField(max_length=255)),
                ('app_date', models.DateField()),
                ('time_book', models.TextField(max_length=25)),
            ],
        ),
    ]

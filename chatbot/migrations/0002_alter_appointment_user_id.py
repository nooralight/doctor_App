# Generated by Django 4.0.6 on 2022-08-01 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='user_id',
            field=models.TextField(max_length=25),
        ),
    ]

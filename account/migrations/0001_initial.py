# Generated by Django 4.0.6 on 2022-07-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.TextField(max_length=255)),
                ('password', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('isAdmin', models.CharField(default='0', max_length=2)),
            ],
        ),
    ]

# Generated by Django 2.2.16 on 2021-08-13 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20210813_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, error_messages={'unique': 'A user with that email already exists.'}, max_length=254, null=True, unique=True, verbose_name='Email address'),
        ),
    ]

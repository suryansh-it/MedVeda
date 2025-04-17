# Generated by Django 5.2 on 2025-04-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remedies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='remedy',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]

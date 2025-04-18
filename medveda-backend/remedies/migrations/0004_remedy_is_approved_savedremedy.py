# Generated by Django 5.2 on 2025-04-18 19:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remedies', '0003_review'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='remedy',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='SavedRemedy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('remedy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remedies.remedy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'remedy')},
            },
        ),
    ]

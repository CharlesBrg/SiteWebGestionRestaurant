# Generated by Django 5.0.1 on 2024-05-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]

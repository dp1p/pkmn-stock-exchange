# Generated by Django 5.0.3 on 2024-08-19 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]

# Generated by Django 5.0.3 on 2024-08-15 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pkmnstock_app', '0015_pkmnstock_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pkmnstock',
            name='details',
        ),
    ]

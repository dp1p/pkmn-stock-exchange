# Generated by Django 5.0.3 on 2024-08-16 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkmnstock_app', '0019_pkmnstock_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pkmnstock',
            name='evolution_stages',
            field=models.JSONField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.0.3 on 2024-08-14 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkmnstock_app', '0005_remove_pkmnstock_base_price_remove_pkmnstock_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pkmnstock',
            name='base_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

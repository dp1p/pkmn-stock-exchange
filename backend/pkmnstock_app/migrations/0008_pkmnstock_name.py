# Generated by Django 5.0.3 on 2024-08-14 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkmnstock_app', '0007_remove_pkmnstock_base_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='pkmnstock',
            name='name',
            field=models.CharField(default='DoesNotExist', max_length=255),
        ),
    ]

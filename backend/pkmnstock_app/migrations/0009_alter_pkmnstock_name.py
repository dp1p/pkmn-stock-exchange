# Generated by Django 5.0.3 on 2024-08-14 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkmnstock_app', '0008_pkmnstock_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pkmnstock',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]

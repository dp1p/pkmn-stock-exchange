# Generated by Django 5.0.3 on 2024-08-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_rename_shares_purchased_pkmnportfolio_shares_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pkmnportfolio',
            name='shares',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_clientdetails_city_clientdetails_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetails',
            name='skilles',
            field=models.TextField(null=True),
        ),
    ]

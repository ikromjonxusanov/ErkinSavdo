# Generated by Django 3.2.2 on 2021-06-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erkinSavdoApp', '0003_auto_20210522_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='priceType',
            field=models.CharField(choices=[('UZS', 'UZS'), ('RUB', 'RUB'), ('USD', 'USD')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='rentOrSent',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Rent m', 'Rent m'), ('Rent w', 'Rent w'), ('Rent d', 'Rent d')], max_length=255),
        ),
    ]
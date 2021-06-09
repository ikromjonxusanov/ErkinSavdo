# Generated by Django 3.2.2 on 2021-06-09 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erkinSavdoApp', '0005_home_lengthofrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='erkinSavdoApp.customer'),
        ),
        migrations.AlterField(
            model_name='home',
            name='rentOrSent',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Rent m', 'Rent month'), ('Rent w', 'Rent week'), ('Rent d', 'Rent day')], max_length=255),
        ),
        migrations.AlterField(
            model_name='home',
            name='typeOfHouse',
            field=models.CharField(choices=[('Flat', 'Flat'), ('House', 'House'), ('Office', 'Office'), ('Shop', 'Shop')], max_length=255),
        ),
    ]

# Generated by Django 3.2.2 on 2021-05-19 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erkinSavdoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='createDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]

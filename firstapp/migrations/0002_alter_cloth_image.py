# Generated by Django 3.2.10 on 2022-01-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='Image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
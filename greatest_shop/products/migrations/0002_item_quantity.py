# Generated by Django 4.0.5 on 2022-06-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]

# Generated by Django 2.1.2 on 2018-12-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_options', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoption',
            name='photos',
            field=models.ImageField(blank=True, upload_to='option'),
        ),
    ]

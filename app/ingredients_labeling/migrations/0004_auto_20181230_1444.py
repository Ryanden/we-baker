# Generated by Django 2.1.3 on 2018-12-30 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients_labeling', '0003_auto_20181230_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientslabeling',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

# Generated by Django 2.1.3 on 2018-12-30 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('costcalculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='costcalculator',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calculators', to='costcalculator.Item', verbose_name='제품'),
        ),
        migrations.AddField(
            model_name='costcalculator',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calculators', to='costcalculator.Material', verbose_name='재료'),
        ),
        migrations.AddField(
            model_name='costcalculator',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calculators', to=settings.AUTH_USER_MODEL),
        ),
    ]

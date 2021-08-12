# Generated by Django 3.2.5 on 2021-07-24 19:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karl_Shop', '0014_alter_shopitems_off_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitems',
            name='off_percentage',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='off_percentage(optional)'),
        ),
    ]
# Generated by Django 3.2.5 on 2021-07-29 07:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karl_Shop', '0037_coupons_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='off_percentage',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
# Generated by Django 3.2.5 on 2021-07-29 07:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karl_Shop', '0036_coupons'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupons',
            name='percentage',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]

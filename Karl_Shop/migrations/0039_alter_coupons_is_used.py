# Generated by Django 3.2.5 on 2021-07-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karl_Shop', '0038_order_off_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupons',
            name='is_used',
            field=models.BooleanField(),
        ),
    ]
# Generated by Django 3.2.5 on 2021-07-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karl_Shop', '0024_alter_order_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='count',
            field=models.IntegerField(null=True),
        ),
    ]

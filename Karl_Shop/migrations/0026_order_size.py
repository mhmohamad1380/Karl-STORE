# Generated by Django 3.2.5 on 2021-07-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karl_Shop', '0025_order_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.IntegerField(null=True),
        ),
    ]
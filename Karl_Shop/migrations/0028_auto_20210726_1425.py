# Generated by Django 3.2.5 on 2021-07-26 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karl_Shop', '0027_alter_order_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, to='Karl_Shop.ShopItems'),
        ),
    ]

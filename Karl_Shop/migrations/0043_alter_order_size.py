# Generated by Django 3.2.5 on 2021-08-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karl_Shop', '0042_alter_order_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]

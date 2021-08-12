# Generated by Django 3.2.5 on 2021-07-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karl_Shop', '0007_headersetting_offers_socialaccounts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headersetting',
            name='accounts',
            field=models.ManyToManyField(blank=True, to='Karl_Shop.SocialAccounts'),
        ),
        migrations.AlterField(
            model_name='headersetting',
            name='offers',
            field=models.ManyToManyField(blank=True, to='Karl_Shop.Offers'),
        ),
    ]
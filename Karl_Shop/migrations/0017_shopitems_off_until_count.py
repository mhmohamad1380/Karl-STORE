# Generated by Django 3.2.5 on 2021-07-24 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karl_Shop', '0016_auto_20210725_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopitems',
            name='off_until_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

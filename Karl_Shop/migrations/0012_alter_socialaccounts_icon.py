# Generated by Django 3.2.5 on 2021-07-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karl_Shop', '0011_alter_socialaccounts_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccounts',
            name='icon',
            field=models.CharField(choices=[('Facebook', 'Facebook'), ('twitter', 'Twitter'), ('google-plus', 'Google Plus'), ('github', 'Github'), ('pinterest', 'Pinterest'), ('linkedin', 'LinkedIn'), ('instagram', 'Instagram'), ('vimeo', 'Vimeo'), ('tumblr', 'Tumblr'), ('skype', 'Skype'), ('youtube', 'YouTube'), ('snapchat', 'Snapchat'), ('telegram', 'Telegram')], max_length=120),
        ),
    ]
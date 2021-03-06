# Generated by Django 3.2.5 on 2021-07-24 15:01

import Karl_Shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karl_Shop', '0006_remove_shopitems_image5'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220, null=True)),
                ('link', models.URLField(null=True, verbose_name='link(optional)')),
                ('description', models.TextField(null=True, verbose_name='description(optional)')),
            ],
        ),
        migrations.CreateModel(
            name='SocialAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('url', models.URLField(null=True)),
                ('icon', models.IntegerField(choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('google-plus', 'Google Plus'), ('github', 'Github'), ('pinterest', 'Pinterest'), ('linkedin', 'LinkedIn'), ('instagram', 'Instagram'), ('vimeo', 'Vimeo'), ('tumblr', 'Tumblr'), ('skype', 'Skype'), ('youtube', 'YouTube'), ('snapchat', 'Snapchat')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeaderSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(null=True, upload_to=Karl_Shop.models.image_path_logo)),
                ('phone_number', models.IntegerField(null=True)),
                ('accounts', models.ManyToManyField(blank=True, null=True, to='Karl_Shop.SocialAccounts')),
                ('offers', models.ManyToManyField(blank=True, null=True, to='Karl_Shop.Offers')),
            ],
        ),
    ]

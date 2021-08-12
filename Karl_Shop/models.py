import os
import random

from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.core.exceptions import *

choices = (
    (0, 'UnAvailable'),
    (1, 'Available')
)


def get_filename(basename):
    basename1 = os.path.basename(basename)
    name, ext = os.path.splitext(basename1)
    return name, ext


def image_path(instance, filename):
    new_name = random.randint(1, 1000000)
    name, ext = get_filename(filename)
    new_name1 = f'blog_{new_name}.{ext}'
    return f"blog/{new_name1}"


# Create your models here.
class Sizes(models.Model):
    size = models.CharField(null=True, blank=False, max_length=2)

    class Meta:
        ordering = ['size']

    def __str__(self):
        return self.size


class Category(models.Model):
    title = models.CharField(null=True, blank=False, max_length=120)

    def __str__(self):
        return self.title


class ShopItems(models.Model):
    title = models.CharField(max_length=120, null=True, blank=False)
    price = models.CharField(null=True, blank=False, max_length=10)
    off_percentage = models.IntegerField(null=True, blank=False, validators=[validators.MinValueValidator(0),
                                                                             validators.MaxValueValidator(100)],
                                         verbose_name='off_percentage(optional)')
    off_until_count = models.IntegerField(null=True, blank=True)
    price_after_off = models.IntegerField(blank=True, null=True,
                                          verbose_name="final Price (dont change it)")
    count = models.IntegerField(null=True, blank=False, validators=[
        validators.MinValueValidator(0)
    ])
    is_available = models.IntegerField(choices=choices)

    sizes = models.ManyToManyField(Sizes, blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    information = models.TextField(null=True, blank=False)
    image1 = models.ImageField(upload_to=image_path, null=True, blank=False)
    image2 = models.ImageField(upload_to=image_path, null=True, blank=True)
    image3 = models.ImageField(upload_to=image_path, null=True, blank=True)
    image4 = models.ImageField(upload_to=image_path, null=True, blank=True)

    def clean(self):
        if self.off_percentage:
            self.price_after_off = int(float(self.price) - (float(self.price) * float(self.off_percentage) / 100))
        else:
            self.price_after_off = float(self.price)
        if self.off_percentage and not self.off_until_count:
            raise ValidationError('if you set off_percentage, you have to set off until count too ')
        elif not self.off_percentage and self.off_until_count:
            raise ValidationError('if you set off until count, you have to set off_percentage too ')
        if not self.off_percentage == 0:
            if self.off_until_count and self.count:
                if self.off_until_count > self.count:
                    raise ValidationError('off until count should be less than product count')
        if not self.image1 or not self.image2:
            raise ValidationError('You have to set both image 1 and image 2')

    def get_absolute_url(self):
        return f'{self.title.replace(" ", "-")}/{self.id}'

    def __str__(self):
        return self.title


socialChoices = (
    ('Facebook', 'Facebook'), ('twitter', 'Twitter'), ('google-plus', 'Google Plus'), ('github', 'Github'),
    ('pinterest', 'Pinterest'), ('linkedin', 'LinkedIn'),
    ('instagram', 'Instagram'), ('vimeo', 'Vimeo'), ('tumblr', 'Tumblr'), ('skype', 'Skype'), ('youtube', 'YouTube'),
    ('snapchat', 'Snapchat'),
    ('telegram', 'Telegram'),
    ('book', 'Portfolio'),
)


class SocialAccounts(models.Model):
    title = models.CharField(max_length=50, null=True, blank=False)
    url = models.URLField(null=True, blank=False)
    icon = models.CharField(choices=socialChoices, max_length=120)

    def __str__(self):
        return self.title


class Offers(models.Model):
    title = models.CharField(max_length=220, null=True, blank=False)
    link = models.URLField(null=True, blank=True, verbose_name='link(optional)')
    description = models.TextField(null=True, blank=True, verbose_name='description(optional)')

    def __str__(self):
        return self.title


def image_path_logo(instance, filename):
    new_name = random.randint(1, 1000000)
    name, ext = get_filename(filename)
    new_name1 = f'blog_{new_name}.{ext}'
    return f'logo/{new_name1}'


class HeaderSetting(models.Model):
    logo = models.ImageField(upload_to=image_path_logo, null=True, blank=False)
    phone_number = models.CharField(max_length=13, null=True, blank=False)
    accounts = models.ManyToManyField(SocialAccounts, blank=True)
    offers = models.ManyToManyField(Offers, blank=True)

    def __str__(self):
        return self.phone_number


def image_path_offers(instance, filename):
    new_name = random.randint(1, 1000000)
    name, ext = get_filename(filename)
    new_name1 = f'blog_{new_name}.{ext}'
    return f"offers/{new_name1}"


class HomePageOffers(models.Model):
    title = models.CharField(max_length=120, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    image = models.ImageField(upload_to=image_path_offers)
    link = models.URLField(null=True, blank=False)

    def clean(self):
        if self.image.width < 1920 or self.image.height < 1280:
            raise ValidationError('please use image with width 1920px and height 1280px')

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    products = models.ForeignKey(ShopItems, blank=False, on_delete=models.CASCADE)
    size = models.CharField(max_length=4, null=True, blank=True)
    count = models.IntegerField(null=True, blank=False)
    final_price = models.FloatField(max_length=10, blank=True, null=True)
    off_percentage = models.IntegerField(null=True, blank=False,
                                         validators=[validators.MaxValueValidator(100),
                                                     validators.MinValueValidator(0)], default=0)

    is_paid = models.BooleanField(default=False, verbose_name='is paid')
    is_checked = models.BooleanField(default=False)

    def clean(self):
        self.final_price = int(self.products.price_after_off) * self.count

    def __str__(self):
        return self.user.username


class Coupons(models.Model):
    title = models.CharField(max_length=20, null=True, blank=False, unique=True)
    percentage = models.IntegerField(null=True, blank=False,
                                     validators=[validators.MaxValueValidator(100), validators.MinValueValidator(1)])
    is_used = models.IntegerField(choices=((1, 'not Used'), (0, 'Used')), default=1)

    def __str__(self):
        return self.title

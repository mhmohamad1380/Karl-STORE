from django.contrib import admin

# Register your models here.
from Karl_Shop.models import ShopItems, Sizes, Category, Offers, SocialAccounts, HeaderSetting, HomePageOffers, Order, \
    Coupons


class ShopAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'image1', 'off_percentage', 'is_available']
    list_editable = ['off_percentage', 'is_available']


class Orders(admin.ModelAdmin):
    list_display = ['__str__', 'is_paid', 'is_checked']


class CouponAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_used']


admin.site.register(ShopItems, ShopAdmin)
admin.site.register(Sizes)
admin.site.register(Category)
admin.site.register(Offers)
admin.site.register(SocialAccounts)
admin.site.register(HeaderSetting)
admin.site.register(HomePageOffers)
admin.site.register(Order, Orders)
admin.site.register(Coupons, CouponAdmin)

import itertools
import json

import requests
from azbankgateways import bankfactories
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from Karl_Shop.models import HeaderSetting, ShopItems, Category, HomePageOffers, Order

from azbankgateways import bankfactories, models as bank_models, default_settings as settings


def homepage(request):
    offers: HomePageOffers = HomePageOffers.objects.all()
    more_off = ShopItems.objects.all()
    print(more_off)
    items: ShopItems = ShopItems.objects.filter(is_available=1).all()[:6]
    categories = Category.objects.all()

    def mygrouper(n, iterable):
        args = [iter(iterable)] * n
        return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

    context = {
        'items': mygrouper(6, items),
        'categories': categories,
        'more_off': more_off.order_by('-off_percentage')[0],
        'more_count': more_off.order_by('-count')[0],
        'offers': offers
    }

    return render(request, 'index.html', context)


def header(request):
    total_price = 0

    settings: HeaderSetting = HeaderSetting.objects.first()
    orders = Order.objects.filter(is_paid=False, user=request.user).all()
    count = orders.count()
    for item in orders:
        total_price += item.final_price

    context = {
        'settings': settings,
        'orders': orders,
        'total_price': total_price,
        'count': count
    }
    return render(request, 'base/header.html', context)


def footer(request):
    settings: HeaderSetting = HeaderSetting.objects.first()
    context = {
        'settings': settings
    }
    return render(request, 'base/footer.html', context)


def clear_cart_list(request):
    filtered_orders = Order.objects.filter(user=request.user).all()
    for order in filtered_orders:
        order.delete()
    return redirect('/cart')


def delete_item(request, Id, *args, **kwargs):
    print(Id)
    filtered_orders: Order = Order.objects.filter(user=request.user, products_id=Id).first()
    print(filtered_orders)
    filtered_orders.delete()
    return redirect('/cart')


def go_to_gateway_view(request):
    if not request.user.is_authenticated:
        raise Http404('You are not Logged in')
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = 0
    for order in Order.objects.filter(user=request.user, is_paid=False).all():
        amount += order.final_price
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    # user_mobile_number = '+989112221234'  # اختیاری
    dollar_price = requests.get('https://api.navasan.tech/latest/?api_key=Oz7vCIKJXT4vh7MmeTROncbmVMKfg7Og')
    jsoend = json.loads(dollar_price.content)
    amount = amount * 10 * int(jsoend['usd_farda_sell']['value'])
    factory = bankfactories.BankFactory()
    bank = factory.create(bank_models.BankType.IDPAY)  # or factory.create(bank_models.BankType.BMI) or set identifier
    bank.set_request(request)
    bank.set_amount(amount)
    # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
    bank.set_client_callback_url('/callback-gateway')
    # bank.set_mobile_number(user_mobile_number)  # اختیاری

    # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
    # پرداخت برقرار کنید.
    bank_record = bank.ready()

    # هدایت کاربر به درگاه بانک
    return bank.redirect_gateway()


def callback_gateway_view(request):
    if not request.user.is_authenticated:
        raise Http404('You are not Logged in')
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        raise Http404
    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        for order in Order.objects.filter(user=request.user, is_paid=False).all():
            order.is_paid = True
            order.save()
        return HttpResponse("پرداخت با موفقیت انجام شد.")

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse(
        "پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")

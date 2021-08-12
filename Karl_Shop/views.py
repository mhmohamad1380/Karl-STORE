import itertools

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import *

# Create your views here.
from Karl_Shop.models import ShopItems, Order, Sizes, Coupons


def sidebar(request):
    sizes = Sizes.objects.all()
    last = ShopItems.objects.order_by('-off_percentage').all()[:3]
    return render(request, 'sidebar.html', {'items': last, 'sizes': sizes})


class ShopList(ListView):
    paginate_by = 6
    template_name = 'shop.html'

    def get_queryset(self):
        return ShopItems.objects.all()


@login_required(login_url='/user/login')
def productDetail(request, title, id, *args, **kwargs):
    print(id)
    product: ShopItems = ShopItems.objects.filter(title=title.replace("-", " "), id=id).first()

    sizes_list = []
    order_list = []
    for order in Order.objects.filter(is_paid=False, user=request.user).all():
        order_list.append(order.products)
    for size in product.sizes.all():
        sizes_list.append(size)
    # add to cart
    if 'sizes' in request.POST:
        user = request.user
        size = request.POST['sizes']
        count = request.POST['quantity']
        Order.objects.create(user=user, products=product, size=size, count=count,
                             final_price=int(product.price_after_off) * int(count))
        return redirect(f'/cart')
    # end add to cart
    if product.count == 0:
        product.is_available = 0
        product.save()
    elif product.count != 0:
        product.is_available = 1
        product.save()
    if product.count == product.off_until_count:
        product.off_percentage = 0
        product.save()
    sizes = []

    for size in product.sizes.all():
        sizes.append(size)

    if product is None:
        raise Http404('Nothing found')
    context = {
        'product': product,
        'price_off': None,
        'sizes': sizes,
        'size_count': len(sizes_list),
        'order_list': order_list
    }
    if product.off_percentage > 0:
        context['price_off'] = int(float(product.price) - (float(product.price) * float(product.off_percentage) / 100))
    return render(request, 'productDetail.html', context)


def related(request, *args, **kwargs):
    searched = request.META.get('PATH_INFO').split('/')[3]
    all_products = ShopItems.objects.all()
    products_searched = ShopItems.objects.filter(id=searched).first()
    products = []

    def mygrouper(n, iterable):
        args = [iter(iterable)] * n
        return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

    for item in all_products:
        for category in item.categories.all():
            if category in products_searched.categories.all():
                if item.title != products_searched.title:
                    products.append(item)
    context = {
        'items': mygrouper(6, products)
    }
    return render(request, 'related_products.html', context)


@login_required(login_url='/user/login')
def cart(request):
    # Updating List
    if 'csrfmiddlewaretoken' in request.POST:
        orderList = []
        for order in Order.objects.filter(is_paid=False).all():
            orderList.append(f'{order.products.title}_{order.id}')

        for item in orderList:
            if f'quantity_{item}' in request.POST:
                items = item.split('_')
                print(items)
                order_1 = Order.objects.get(id=items[1])
                order_1.count = request.POST[f'quantity_{item}']
                order_1.final_price = int(order_1.products.price) * int(request.POST[f'quantity_{item}'])
                order_1.save()
        return redirect('/cart')

    # End Updating List
    orders = Order.objects.filter(user=request.user,is_paid=False).all()
    order_price = 0
    shipping_price = None
    all_price = None
    if 'coupon' in request.POST:
        print('is')
        coupon = request.POST['coupon']
        filtered = Coupons.objects.filter(title=coupon, is_used=1)
        if filtered.exists():
            filtered_first = filtered.first()
            for order in orders:
                order.off_percentage = filtered.first().percentage

                order.save()
            filtered_first.is_used = 0
            print(filtered_first.is_used)
            filtered_first.save()
        return redirect('/cart')
    for order in orders:
        order_price += order.final_price - (order.final_price * order.off_percentage / 100)
    if order_price > 1000:
        shipping_price = "FREE"
        all_price = order_price
    else:
        shipping_price = order_price / 10
        shipping_price = int(shipping_price)
        all_price = shipping_price + order_price

    context = {
        'orders': orders,
        'order_price': order_price,
        'shipping_price': shipping_price,
        'all_price': all_price,
    }
    return render(request, 'cart.html', context)

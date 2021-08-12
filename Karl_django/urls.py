"""Karl_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from azbankgateways.urls import az_bank_gateways_urls
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Karl_Shop.views import related
from . import views, settings
from Karl_Shop.views import cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('accounts/', include("allauth.urls")),
    path('cart', cart),
    path('cart/clear_list', views.clear_cart_list),
    path('header', views.header, name='header'),
    path('footer', views.footer, name='footer'),
    path('related', related, name='related'),
    path('shop/', include("Karl_Shop.urls")),
    path('cart/deleteitem/<int:Id>', views.delete_item),
    path('user/', include("Karl_Account.urls")),
    path('bankgateways/', az_bank_gateways_urls()),
    path('payment/', views.go_to_gateway_view),
    path('callback-gateway/', views.callback_gateway_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

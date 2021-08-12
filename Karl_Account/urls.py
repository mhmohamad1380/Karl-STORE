from django.conf.urls.static import static
from django.urls import path

from Karl_django import settings
from . import views

urlpatterns = [
    path('login', views.login_view),
    path('register', views.register_view),
    path('logout', views.log_out),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

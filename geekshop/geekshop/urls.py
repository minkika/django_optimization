import debug_toolbar

import mainapp.views as mainapp
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from geekshop import settings

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('', include('social_django.urls', namespace='social')),
    path('product/', mainapp.product, name='product'),
    path('catalog/', include('mainapp.urls', namespace='catalog')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('admin/', include('adminapp.urls', namespace='admin')),
    path('order/', include('ordersapp.urls', namespace='order')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

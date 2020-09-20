import mainapp.views as mainapp
from django.urls import path
from django.views.decorators.cache import cache_page

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.catalog, name='index'),
    path('category/<int:pk>/', cache_page(3600)(mainapp.catalog), name='category'),
    path('category/<int:pk>/ajax/', cache_page(3600)(mainapp.products_ajax)),
    path('category/<int:pk>/<int:page>/', mainapp.catalog, name='page'),
    path('product/<int:pk>/', mainapp.product, name='product'),
    path('category/<int:pk>/page/<int:page>/ajax/', cache_page(3600)(mainapp.products_ajax)),
]

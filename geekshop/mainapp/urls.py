import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.catalog, name='index'),
    path('category/<int:pk>/', mainapp.catalog, name='category'),
    path('category/<int:pk>/<int:page>/', mainapp.catalog, name='page'),
    path('product/<int:pk>/', mainapp.product, name='product'),
]

from django.urls import path
from adminapp.views import users, categories, products

app_name = 'adminapp'
urlpatterns = [
    path('users/read/', users.UserListView.as_view(), name='users'),
    path('users/delete/<int:pk>', users.UserDeleteView.as_view(), name='user_delete'),

    path('categories/create', categories.ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', categories.ProductCategoryListView.as_view(), name='categories'),
    path('categories/update/<int:pk>', categories.ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>', categories.ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/category/<int:pk>', products.product_create, name='product_create'),
    path('products/read/category/<int:pk>', products.products, name='products'),
    path('products/read/<int:pk>', products.ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>', products.product_update, name='product_update'),
    path('products/delete/<int:pk>', products.ProductDeleteView.as_view(), name='product_delete'),
]


from django import template

from geekshop.settings import MEDIA_URL

register = template.Library()


def media_folder_products(string):
    if not string:
        string = 'product_images/default.png'
    return f'{MEDIA_URL}{string}'


register.filter('media_folder_products', media_folder_products)


@register.filter(name='media_folder_users')
def media_folder_users(string):
    if not string:
        string = 'users_avatars/default.png'
    return f'{MEDIA_URL}{string}'

from attr.filters import exclude

from authapp.forms import ShopUserEditForm

from authapp.models import ShopUser
from django import forms

from mainapp.models import ProductCategory, Product


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


class ProductCategoryEditForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductCategoryEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

class ProductAdminEditForm(ShopUserEditForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'image', 'short_desc', 'description', 'price', 'quantity', 'is_active',)
        # exclude = exclude('password',)
        # exclude = ('password',)
        # exclude = ['password']
        # fields = exclude('password')

    def __init__(self, *args, **kwargs):
        super(ProductAdminEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
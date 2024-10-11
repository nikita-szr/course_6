from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите наименование продукта'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control-file'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })

    def clean_name(self):
        name = self.cleaned_data['name']
        for word in self.banned_words:
            if word.lower() in name.lower():
                raise ValidationError(f"Запрещено использовать слово '{word}'")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        for word in self.banned_words:
            if word.lower() in description.lower():
                raise forms.ValidationError(f"Запрещено использовать слово '{word}'")
        return description

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной.")
        return price

from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

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

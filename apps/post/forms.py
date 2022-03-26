from django import forms
from django.db.models import fields



class SearchForm(forms.Form):
    query = forms.CharField(required=False,max_length=50, widget=forms.TextInput(attrs={
        "placeholder": "Pesquisar", "class": "form-control me-2", "type":"search"}), label="Pesquisar")


# class ProductForm(forms.ModelForm):
    
#     class Meta:
#         model = Product
#         fields = ["available", "category", "description", "image", "ingredient", "name", "price"]
         


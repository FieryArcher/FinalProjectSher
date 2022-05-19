from .models import *
from django.forms import ModelForm, TextInput, DateInput, Textarea, FileField, NumberInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Clients
        fields = ['client_name', 'client_address', 'client_phone', 'waiter_id']

        widgets = {
            'client_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full name'
            }),

            'client_address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            }),

            'client_phone': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }),
            'waiter_id': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Waiter id',
                'options': 'customer_waiter_id'
            }),

        }


class ProvideForm(ModelForm):
    class Meta:
        model = Provide
        fields = ['provides_id', 'provides_supplier_id', 'provides_ingredients_name', 'provides_number', 'data']

        widgets = {
            'provides_id': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID'
            }),

            'provides_supplier_id': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Supplier_id '
            }),

            'provides_ingredients_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingredients name '
            }),
            'provides_number': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Weight',

            }),
            'data': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date',
            }),
        }


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

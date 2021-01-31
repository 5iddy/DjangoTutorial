from .models import Account
from django.forms import ModelForm
from django import forms
from django.forms import widgets
import re

class UserRegistrationForm(ModelForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(widget=widgets.EmailInput)
    username=forms.CharField(max_length=200, required=True, widget=widgets.TextInput)
    password1= forms.CharField(max_length=200, required=True, widget=widgets.PasswordInput)
    password2 = forms.CharField(max_length=200, required=True, widget=widgets.PasswordInput)

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'profile_picture', 'country', 'phone_number', 'website']

    def is_valid(self):
        form_validity = super().is_valid()
        if form_validity:
            if self.check_phone_number():
                return True
            else:
                return False
        else:
            return False


    def check_phone_number(self):
        pattern = re.compile(r'^\d{10}$')
        if pattern.fullmatch(self.data['phone_number']):
            self.cleaned_data['phone_number'] = self.data['phone_number']
            return True
        else:
            return False
from django.contrib.auth.models import User
from .models import *
from django.forms import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['first_name'].label = ""
        self.fields['last_name'].label = ""
        self.fields['email'].label = ""
        self.fields['password'].label = ""
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].label = ""

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class LoginForm(Form):
    username = CharField(max_length=255)
    password = CharField(max_length=255, widget=PasswordInput())
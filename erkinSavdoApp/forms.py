from django.contrib.auth.models import User
from .models import *
from django.forms import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['email'].label = ""
        self.fields['password'].label = ""
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class ChangeUser(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['first_name'].label = ""
        self.fields['last_name'].label = ""
        self.fields['email'].label = ""
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['phone', 'profilePicture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].label = ""
        self.fields['profilePicture'].label = ""

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class LoginForm(Form):
    username = CharField(max_length=255)
    password = CharField(max_length=255, widget=PasswordInput())

class HomeForm(ModelForm):
    class Meta:
        model = Home
        fields = "__all__"
        exclude = ['author', 'status']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['title'].label = ""
        # self.fields['description'].label = ""
        # self.fields['price'].label = ""
        # self.fields['address'].label = ""
        self.fields['image'].label = ""
        # self.fields['region'].label = ""
        # self.fields['area'].label = ""
        self.fields['rentOrSent'].label = ""
        self.fields['typeOfHouse'].label = ""
        self.fields['priceType'].label = ""
        self.fields['lengthOfRooms'].label = ""



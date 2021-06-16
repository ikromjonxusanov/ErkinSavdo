from django.contrib.auth.models import User
from .models import *
from django.forms import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MaxLengthValidator

class UserForm(ModelForm):
    password = CharField(widget=PasswordInput(),validators=[MinLengthValidator(8)])
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['username'].label = _("Username")
        self.fields['email'].label = _("Email")
        self.fields['password'].label = _("Password")
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class ChangeUser(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = _("Username")
        self.fields['first_name'].label = _("First name")
        self.fields['last_name'].label = _("Last name")
        self.fields['email'].label = _("Email")
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['phone', 'profilePicture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].label = _("Phone")
        self.fields['profilePicture'].label = _("Profile image")

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class LoginForm(Form):
    username = CharField(max_length=255, label=_('Username'))
    password = CharField(max_length=255, widget=PasswordInput(), label=_('Password'))
class HomeForm(ModelForm):
    class Meta:
        model = Home
        fields = "__all__"
        exclude = ['author', 'status']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = _("Title")
        self.fields['description'].label = _("Description")
        self.fields['price'].label = _("Price")
        self.fields['address'].label = _("Address")
        self.fields['image'].label = _("Image")
        self.fields['area'].label = _("Home area")
        self.fields['rentOrSale'].label = _("Rent or Sale")
        self.fields['typeOfHouse'].label = _("Home type")
        self.fields['priceType'].label = _("Price type")
        self.fields['lengthOfRooms'].label = _("Rooms length")



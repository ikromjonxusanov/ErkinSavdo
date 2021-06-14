from django.db.models import *
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Province(Model):
    language = CharField(max_length=255, choices=(('uz', "UZ"),  ('en', 'EN')))
    name = CharField(max_length=255)
    def __str__(self):
        return self.name

class District(Model):
    language = CharField(max_length=255, choices=(('uz', "UZ"), ('en', 'EN')))
    province = ForeignKey(Province, on_delete=CASCADE)
    name = CharField(max_length=255)
    def __str__(self):
        return self.province.name+" ("+self.name+")"

class PriceType(Model):
    name = CharField(max_length=255)
    def __str__(self):
        return self.name

class HomeType(Model):
    language = CharField(max_length=255, choices=(('uz', "UZ"), ('en', 'EN')))
    name = CharField(max_length=255)
    def __str__(self):
        return self.name

class Customer(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    profilePicture = ImageField(upload_to='profilePic', default="default-user.png")
    phone = PhoneNumberField(unique=True)
    def __str__(self):
        return self.user.username

class Home(Model):
    author = ForeignKey(Customer, on_delete=CASCADE, null=True)
    title = CharField(max_length=255)
    description = TextField()
    price = FloatField()
    address = ForeignKey(District, on_delete=SET_NULL, null=True)
    image = ImageField(upload_to="home/images", default='default-home.png')
    area = FloatField(default=0)
    rentOrSale = CharField(max_length=255, choices=(('Sale', 'Sale'), ('Rent m', 'Rent month'), ('Rent w', 'Rent week'), ('Rent d', 'Rent day'), ))
    typeOfHouse = ForeignKey(HomeType, on_delete=SET_NULL, null=True)
    priceType = ForeignKey(PriceType, on_delete=SET_NULL, null=True)
    lengthOfRooms = IntegerField(default=0, null=True)
    status = BooleanField(default=False)
    createDate = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title







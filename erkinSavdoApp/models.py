from django.db.models import *
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Province(Model):
    name = CharField(max_length=255)
    def __str__(self):
        return self.name

class District(Model):
    province = ForeignKey(Province, on_delete=CASCADE)
    name = CharField(max_length=255)
    def __str__(self):
        return self.province.name+" ("+self.name+")"

class PriceType(Model):
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
    regions = (
        ("Andijon viloyati", "Andijon viloyati"),
        ("Buxoro viloyati", "Buxoro viloyati"),
        ("Jizzax viloyati", "Jizzax viloyati"),
        ("Qashqadaryo viloyati", "Qashqadaryo viloyati"),
        ("Navoiy viloyati", "Navoiy viloyati"),
        ("Namangan viloyati", "Namangan viloyati"),
        ("Samarqand viloyati", "Samarqand viloyati"),
        ("Surxondaryo viloyati", "Surxondaryo viloyati"),
        ("Sirdaryo viloyati", "Sirdaryo viloyati"),
        ("Toshkent viloyati","Toshkent viloyati"),
        ("Farg'ona viloyati","Farg'ona viloyati"),
        ("Xorazm viloyati","Xorazm viloyati"),
        ("Qoraqalpog'iston Respublikasi","Qoraqalpog'iston Respublikasi"),
        ("Toshkent shahri","Toshkent shahri")
    )
    typeOfHouses = (
        ("Flat", "Flat"),
        ("House", "House"),
        ("Office", "Office"),
        ("Shop", "Shop"),
    )
    author = ForeignKey(Customer, on_delete=CASCADE, null=True)
    title = CharField(max_length=255)
    description = TextField()
    price = FloatField()
    address = CharField(max_length=255)
    image = ImageField(upload_to="home/images", default='default-home.png')
    region = ForeignKey(District, on_delete=SET_NULL, null=True)
    area = FloatField(default=0)
    rentOrSent = CharField(max_length=255, choices=(('Sale', 'Sale'), ('Rent m', 'Rent month'), ('Rent w', 'Rent week'), ('Rent d', 'Rent day'), ))
    typeOfHouse = CharField(max_length=255, choices=typeOfHouses)
    priceType = ForeignKey(PriceType, on_delete=SET_NULL, null=True)
    lengthOfRooms = IntegerField(default=0, null=True)
    status = BooleanField(default=False)
    createDate = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title







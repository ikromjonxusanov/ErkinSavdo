from django.db.models import *
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


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
        ("Kvartira", "Kvartira"),
        ("Hovli", "Hovli"),
        ("Ofis", "Ofis"),
        ("Do'kon", "Do'kon"),
    )
    author = ForeignKey(Customer, on_delete=CASCADE)
    title = CharField(max_length=255)
    description = TextField()
    price = FloatField()
    address = CharField(max_length=255)
    image = ImageField(upload_to="home/images", default='default-home.png')
    region = CharField(choices=regions, max_length=255)
    area = FloatField()
    rentOrSent = CharField(max_length=255, choices=(('Sale', 'Sale'), ('Rent m', 'Rent m'), ('Rent w', 'Rent w'), ('Rent d', 'Rent d'), ))
    typeOfHouse = CharField(max_length=255, choices=typeOfHouses)
    priceType = CharField(max_length=255, choices=(
            ("UZS", 'UZS'),
            ("RUB", 'RUB'),
            ("USD", 'USD')
        ), null=True
    )
    lengthOfRooms = IntegerField(default=0, null=True)
    status = BooleanField(default=False)
    createDate = DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class TopHome(Model):
    home = ForeignKey(Home, on_delete=CASCADE)
    price = FloatField()
    createDate = DateTimeField(auto_now_add=True)
    dueDate = DateTimeField()

# class s:
#     from django.db.models import *
#     from phonenumber_field.modelfields import PhoneNumberField
#
#     from django.contrib.auth.models import AbstractUser, BaseUserManager
#     from django.core.validators import RegexValidator
#     from django.db import models
#     from django.utils.translation import ugettext_lazy as _
#
#     # Create your models here.
#     class UserManager(BaseUserManager):
#         """Define a model manager for User model with no username field."""
#
#         use_in_migrations = True
#
#         def create_user(self, phone, password, **extra_fields):
#             """Create and save a User with the given phone and password."""
#             if not phone:
#                 raise ValueError('The given phone must be set')
#             self.phone = phone
#             user = self.model(phone=phone, **extra_fields)
#             user.set_password(password)
#             user.save()
#             return user
#
#         def create_superuser(self, phone, password, **extra_fields):
#             """Create and save a SuperUser with the given phone and password."""
#             extra_fields.setdefault('is_active', True)
#             extra_fields.setdefault('is_staff', True)
#             extra_fields.setdefault('is_superuser', True)
#
#             if extra_fields.get('is_staff') is not True:
#                 raise ValueError('Superuser must have is_staff=True.')
#             if extra_fields.get('is_superuser') is not True:
#                 raise ValueError('Superuser must have is_superuser=True.')
#
#             return self._create_user(phone, password, **extra_fields)
#
#     class CustomUser(AbstractUser):
#         """User model."""
#
#         username = None
#         email = models.EmailField(blank=True, null=True)
#         phone = PhoneNumberField(unique=True)  # validators should be a list
#
#         USERNAME_FIELD = 'phone'
#         REQUIRED_FIELDS = ['email']
#
#         objects = UserManager()
#
#         def __str__(self):
#             return self.email
#
#     class Home(Model):
#         regions = (
#             (1, "Andijon viloyati"),
#             (2, "Buxoro viloyati"),
#             (3, "Jizzax viloyati"),
#             (4, "Qashqadaryo viloyati"),
#             (5, "Navoiy viloyati"),
#             (6, "Namangan viloyati"),
#             (7, "Samarqand viloyati"),
#             (8, "Surxondaryo viloyati"),
#             (9, "Sirdaryo viloyati"),
#             (10, "Toshkent viloyati"),
#             (11, "Farg'ona viloyati"),
#             (12, "Xorazm viloyati"),
#             (13, "Qoraqalpog'iston Respublikasi"),
#             (14, "Toshkent shahri")
#         )
#         author = ForeignKey(CustomUser, on_delete=CASCADE)
#         title = CharField(max_length=255)
#         description = TextField()
#         price = FloatField()
#         address = CharField(max_length=255)
#         region = CharField(choices=regions, max_length=255)
#         area = FloatField()
#
#         def __str__(self):
#             return self.title



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


admin.site.register(Customer)
admin.site.register(Home)
admin.site.register(PriceType)
admin.site.register(Province)
admin.site.register(District)



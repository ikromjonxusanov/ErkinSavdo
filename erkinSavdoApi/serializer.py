from erkinSavdoApp.models import *
from rest_framework.serializers import *


class ProvinceSerializer(ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"


class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"


class PriceTypeSerializer(ModelSerializer):
    class Meta:
        model = PriceType
        fields = "__all__"


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class HomeSerializer(ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"

class HomeTypeSerializer(ModelSerializer):
    class Meta:
        model = HomeType
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


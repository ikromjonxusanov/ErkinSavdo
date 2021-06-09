from django_filters import *

from .models import Home
from django.db import models
from django.forms import CheckboxInput

class HomeFilter(FilterSet):
    title_filter = CharFilter(field_name='title', lookup_expr='icontains', label="")
    address_filter = CharFilter(field_name='address', lookup_expr='icontains', label="")
    number_filter_gte = NumberFilter(field_name='price', lookup_expr='gte', label="")
    number_filter_lte = NumberFilter(field_name='price', lookup_expr='lte', label="")
    lengthOfRooms_filter_gte = NumberFilter(field_name='lengthOfRooms', lookup_expr='gte', label="")
    lengthOfRooms_filter_lte = NumberFilter(field_name='lengthOfRooms', lookup_expr='lte', label="")
    area_filter_gte = NumberFilter(field_name='area', lookup_expr='gte', label="")
    area_filter_lte = NumberFilter(field_name='area', lookup_expr='lte', label="")

    class Meta:
        model = Home
        fields = "__all__"
        exclude = ['author', 'title', 'description','address', 'area', 'image', 'price', 'lengthOfRooms', 'status', "image2", "image3", "image4", "image5", "image6", "image7", "image8"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)





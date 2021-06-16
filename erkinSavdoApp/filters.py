from django_filters import *
from .models import Home, BooleanField
from .forms import CheckboxInput
from django.utils.translation import gettext_lazy as _

class HomeFilter(FilterSet):
    title_filter = CharFilter(field_name='title', lookup_expr='icontains', label=_("Title"))
    number_filter_gte = NumberFilter(field_name='price', lookup_expr='gte', label=_("Min price"))
    number_filter_lte = NumberFilter(field_name='price', lookup_expr='lte', label=_("Max price"))
    lengthOfRooms_filter_gte = NumberFilter(field_name='lengthOfRooms', lookup_expr='gte', label=_("Min length rooms"))
    lengthOfRooms_filter_lte = NumberFilter(field_name='lengthOfRooms', lookup_expr='lte', label=_("Max length rooms"))
    area_filter_gte = NumberFilter(field_name='area', lookup_expr='gte', label=_("Min home area"))
    area_filter_lte = NumberFilter(field_name='area', lookup_expr='lte', label=_("Max home area"))
    class Meta:
        model = Home
        fields = "__all__"
        exclude = ['author', 'title', 'description', 'area', 'image', 'price', 'lengthOfRooms', 'status']






from django.urls import path
from .views import *
app_name = "api"


urlpatterns = [
    path("", apiHome),
    path('customers/', CustomerGenericMixins.as_view(), name="customers"),
    path('customers/<int:pk>/', CustomerGenericMixins.as_view(), name="customer-detail"),
    path('provinces/', ProvinceGenericMixins.as_view(), name="provinces"),
    path('provinces/<int:pk>/', ProvinceGenericMixins.as_view(), name="province-detail"),
    path('districts/', DistrictGenericMixins.as_view(), name="districts"),
    path('districts/<int:pk>/', DistrictGenericMixins.as_view(), name="district-detail"),
    path('price-types/', PriceTypeGenericMixins.as_view(), name="price-type"),
    path('price-types/<int:pk>/', PriceTypeGenericMixins.as_view(), name="price-type-detail"),
    path('homes/', HomeGenericMixins.as_view(), name="homes"),
    path('homes/<int:pk>/', HomeGenericMixins.as_view(), name="home-detail"),
    path('home-types', HomeTypeGenericMixins.as_view(), name="home-types"),
    path('home-types/<int:pk>/', HomeTypeGenericMixins.as_view(), name="home-type-detail"),
    path('users/', UserGenericMixins.as_view(), name="users"),
    path('users/<int:pk>/', UserGenericMixins.as_view(), name="user-detail"),
]


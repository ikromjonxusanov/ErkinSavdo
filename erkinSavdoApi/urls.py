from django.urls import path
from .views import *
urlpatterns  = [
    path('customers/', CustomerGenericMixins.as_view()),
    path('customers/<int:pk>/', CustomerGenericMixins.as_view()),
    path('provinces/', ProvinceGenericMixins.as_view()),
    path('provinces/<int:pk>/', ProvinceGenericMixins.as_view()),
    path('districts/', DistrictGenericMixins.as_view()),
    path('districts/<int:pk>/', DistrictGenericMixins.as_view()),
    path('price-types/', PriceTypeGenericMixins.as_view()),
    path('price-types/<int:pk>/', PriceTypeGenericMixins.as_view()),
    path('users/', UserGenericMixins.as_view()),
    path('users/<int:pk>/', UserGenericMixins.as_view()),

]


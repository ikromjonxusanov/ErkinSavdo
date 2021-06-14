from .serializer import *
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
##
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
##

def get_object_or_404(model, pk):
    try:
        return model.objects.get(id=pk)
    except:
        return None

class CustomerGenericMixins(GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)

class ProvinceGenericMixins(GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    serializer_class = ProvinceSerializer
    queryset = Province.objects.all()
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)

class DistrictGenericMixins(GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)

class PriceTypeGenericMixins(GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    serializer_class = PriceTypeSerializer
    queryset = PriceType.objects.all()
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)

class HomeGenericMixins(GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)

class UserGenericMixins(GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)

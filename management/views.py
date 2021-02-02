from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics, status
from .models import *
from rest_framework.generics import ListAPIView
from .serializers import *
from rest_framework.generics import CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.
@api_view(['POST'])
def signup(request):
    if request.method == "POST":
        username=request.data['username']
        email=request.data['email']
        password=request.data['password']

        user = User(username=username,email=email)
        user.set_password(password) 
        user.save()
        return Response("success",status=200)

class GetProducts(ListAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()

class GetSearchProducts(ListAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['types']

class GetViewProducts(ListAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    

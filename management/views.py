from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics, status

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
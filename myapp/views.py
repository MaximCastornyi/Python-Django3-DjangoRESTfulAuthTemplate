from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer

from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .permissions import IsEmployee, IsManager

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)



# basic authentication
class HelloAPI(APIView):
    permission_classes = [permissions.IsAuthenticated] 
    def get(self, request): 
        data = {
            'message' : 'Hello Django REST API'
        }       
        return Response(data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def hello_drf(request):
    data = {
            'message' : 'Hello Django REST API. @api_view'
        }       
    return Response(data)


#role-based 
class HelloRoleAPI(APIView):
    permission_classes = [IsEmployee] 
    def get(self, request): 
        data = {
            'message' : 'Hello Django REST API'
        }       
        return Response(data)


@api_view(["GET"])
@permission_classes([IsManager])
def hello_role_drf(request):
    data = {
            'message' : 'Hello Django REST API. @api_view'
        }       
    return Response(data)
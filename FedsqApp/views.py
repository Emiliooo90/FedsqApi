from django.shortcuts import render
from .models import Usuario, Ingrediente, Plato, Orden
from rest_framework import viewsets
from rest_framework import permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
#from knox.models import AuthToken
from knox.auth import AuthToken
from .serializers import UsuarioSerializer, IngredienteSerializer, PlatoSerializer, OrdenSerializer

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class IngredienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow ingredients to be viewed or edited
    """
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlatoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows dishes to be viewed or edited
    """
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrdenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited
    """
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    permission_classes = [permissions.IsAuthenticated]
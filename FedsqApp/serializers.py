from .models import Usuario, Ingrediente, Plato, Orden
from django.contrib.auth.models import User
from rest_framework import serializers, validators

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['url', 'id', 'username', 'email', 'password', 'rol', 'qrImage', 'link']
        #fields = ['id', 'username', 'email']

class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['url', 'nombre_ingrediente', 'descripcion_ingrediente', 'stock', 'otros_detalles_ingrediente']

class PlatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plato
        fields = ['url', 'nombre_plato', 'descripcion_plato', 'precio_plato', 'otros_detalles_plato', 'ingredientes']

class OrdenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orden
        fields = ['url', 'id_mesa', 'estado', 'fecha_creacion', 'otros_detalles_orden', 'id_plato']
    
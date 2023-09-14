from django.contrib import admin
from .models import Usuario, Ingrediente, Plato, Orden

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Ingrediente)
admin.site.register(Plato)
admin.site.register(Orden)

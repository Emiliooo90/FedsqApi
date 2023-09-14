from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.

class Usuario(AbstractUser):
    rol = models.CharField(max_length=30)
    qrImage = models.ImageField(blank=True, upload_to='qr_folder')
    link = models.CharField(max_length=300, default='')

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.link)
        qr_offset = Image.new('RGB', (600, 600), 'white')
        draw = ImageDraw.Draw(qr_offset)
        qr_offset.paste(qr_image)
        files_name = f'{self.id}qr.png'
        buffer = BytesIO()
        qr_offset.save(buffer, 'PNG')
        self.qrImage.save(files_name, File(buffer), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)

class Ingrediente(models.Model):
    nombre_ingrediente = models.CharField(max_length=100)
    descripcion_ingrediente = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    otros_detalles_ingrediente = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_ingrediente

class Plato(models.Model):
    nombre_plato = models.CharField(max_length=100)
    descripcion_plato = models.CharField(max_length=300)
    precio_plato = models.IntegerField(default=0)
    otros_detalles_plato = models.CharField(max_length=100) 
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.nombre_plato

class Orden(models.Model):
    estado = models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField()
    otros_detalles_orden = models.CharField(max_length=100)
    id_plato = models.ForeignKey(Plato, on_delete=models.CASCADE)



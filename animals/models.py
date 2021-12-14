from django.db import models

# Create your models here.
class CatImage(models.Model):
    """ Modelo que representa una instancia de una imagen consultada

        :author: Luis Merizalde - luis.merizalde@outlook.com.com.co
    """
    image_url = models.CharField(verbose_name='url imagen', max_length=200)
    created = models.DateTimeField(auto_now_add=True)
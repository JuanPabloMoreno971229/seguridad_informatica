from django.db import models
from tkinter import *

# Create your models here.
class data_login(models.Model):
   
    mail= models.EmailField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
    class Meta:
        verbose_name = "Dato"
        verbose_name_plural = "Datos"
        
                
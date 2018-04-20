from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Academia(models.Model):
	nombre			= models.CharField(max_length =100)

	def __str__(self):
		return self.nombre



class Entrenador(models.Model):


	nombre		= models.CharField(max_length =100)
	telefono	= models.IntegerField()
	correo		= models.EmailField(max_length=100)

	def __str__ (self):
		return self.nombre

class Equipo(models.Model):
	nombre 		= models.CharField(max_length =100)
	entrenador 	= models.ForeignKey(Entrenador, on_delete=models.CASCADE)


	def __str__(self):
		return self.nombre

class Futbolista (models.Model):


	nombre		= models.CharField(max_length =100)
	correo		= models.EmailField(max_length=100)
	telefono	= models.IntegerField()
	equipo		= models.ForeignKey(Equipo, on_delete=models.CASCADE)
	academia 	= models.ForeignKey(Academia, on_delete=models.CASCADE)
	foto 		= models.ImageField(upload_to='fotos', null= True, blank= True)

	def __str__ (self):
		return self.nombre

class Perfil (models.Model):
	user 	= models.OneToOneField(User, on_delete=models.CASCADE)
	foto 	= models.ImageField(upload_to='perfiles', null=True, blank=True)
	nombre 	= models.CharField(max_length = 100)

	def __str__ (self):
		return self.user.username
from __future__ import unicode_literals
from django.db import models

class Administrador(models.Model):
	codigo = models.IntegerField()		#ATRIBUTOS DE LA CLASE: Administrador
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	correo = models.EmailField(max_length=50)
	#timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


class Director(models.Model):
	codigo = models.IntegerField()
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	correo = models.EmailField(max_length=50)
	codigo_admin = models.ForeignKey(Administrador, null=True, on_delete=models.SET_NULL)

class Maestro(models.Model):
	codigo = models.IntegerField()	
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	correo = models.CharField(max_length=50)
	curso = models.CharField(max_length=50)
	#codigo_director = models.CharField(max_length=50)
	codigo_director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)

class Clase(models.Model):
	codigo = models.IntegerField()
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200)
	codigo_director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)

class Alumno(models.Model):
	codigo = models.IntegerField()
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	correo = models.EmailField(max_length=50)
	codigo_clase = models.ForeignKey(Clase, null=True, on_delete=models.SET_NULL)



#class Deposito(models.Model): #Declaramos una clase deposito que hereda la clase models.Model
#	codigo = models.IntegerField()#Esta clase tiene un código tipo Entero
#	descripcion = models.CharField(max_length=50)#también una descripción (cadena) con un maximo de 50 caracteres


#class Articulo(models.Model):
#	codigo = models.IntegerField()		#ATRIBUTOS DE LA CLASE: Articulo
#	descripcion = models.CharField(max_length=50)
#	cantidad = models.IntegerField()
#	color = models.CharField(max_length=1, choices=COLORES) #2 -> Ver descripiones
#	deposito = models.ForeignKey(Deposito, null=True, on_delete=models.SET_NULL)#3 -> Ver Descripciones

	# 2-Atributo tiene una longitud de 1, 
	#Se utiliza para seleccionar el color mediante el número. 
	#Pertenecen al vector COLORES en la base de datos aparecerá una lista desplegable

	# 3-Atributo del tipo "Llave Foranea", 
	#al eliminar la llave foranea colocará un Null en esa posición 
	#para evitar problemas con las herencias en la base de datos
	#deposito tendrá como llave foranea a la clase Deposito

		

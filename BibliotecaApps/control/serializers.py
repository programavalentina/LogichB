#Vamos a importar las "clases" 
#serializadores que pondrán los atributos de cada clase en serie

from rest_framework import serializers

#Importamos los modelos
from control.models import Administrador, Director, Maestro, Alumno, Clase

#DEFINIMOS LAS CLASES que SERIALIZARÁN LOS DATOS 

#Definimos la Clase que Serializará "Administrador"
class AdministradorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Administrador
		fields = ('id', 'codigo', 'nombres', 'apellidos', 'correo')

#Definimos la Clase que Serializará "Director"
class DirectorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Director
		fields = ('id', 'codigo', 'nombres', 'apellidos', 'correo', 'codigo_admin')

#Definimos la Clase que Serializará "Maestro"
class MaestroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Maestro
		fields = ('id', 'codigo', 'nombres', 'apellidos', 'correo', 'curso', 'codigo_director')

#Definimos la Clase que Serializará "Alumno"
class AlumnoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alumno
		fields = ('id', 'codigo', 'nombres', 'apellidos', 'correo', 'codigo_clase')		

		#Definimos la Clase que Serializará "Alumno"
class ClaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Clase
		fields = ('id', 'codigo', 'nombre', 'descripcion', 'codigo_director')		
#Hacemos uso de la clase "serializers" (import) del "rest_framework",
#y de esta clase utilizamos el módulo: "serializers"
#el modulo tiene la clase "ModelSerializer"
# Desde la cual van a eredar en este caso las 2 clases DepositoSerializer y ArticuloSerializer
# Esto se encargará de acomodar en serie los atributos de cada clase
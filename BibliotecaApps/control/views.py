from django.shortcuts import render, HttpResponse

#importamos 
from rest_framework import generics

from control.models import Administrador, Director, Maestro, Clase, Alumno

from control.serializers import AdministradorSerializer, DirectorSerializer
from control.serializers import MaestroSerializer, AlumnoSerializer, ClaseSerializer

from .forms import FormularioRegistro

def formulario(request):
	form = FormularioRegistro()
	context = {
		"elFormulario":form,
	}
	return render(request, "control/login.html", context)



#Creamos nuestras Views
#LISTA DE ADMINISTRADOR
class AdministradorList(generics.ListCreateAPIView):#Creamos una esta clase que mostrará la Lista de Administrador
	queryset = Administrador.objects.all()
	serializer_class = AdministradorSerializer

#Clase que permitirá RECUPERAR, ACTUALIZAR Y DESTRUIR
#VISTA PARA EL DETALLE DE LOS ADMINISTRADOR
class AdministradorDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Administrador.objects.all()
	serializer_class = AdministradorSerializer

#VISTA - LISTA DE Directores
class DirectorList(generics.ListCreateAPIView):#Creamos una esta clase que mostrará la Lista de Directores
	queryset = Director.objects.all()#
	serializer_class = DirectorSerializer

#Clase que permitirá RECUPERAR, ACTUALIZAR Y DESTRUIR
#VISTA - LISTA DETALLES DE DIRECTORES
class DirectorDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Director.objects.all()
	serializer_class = DirectorSerializer

#VISTA - LISTA DE Profesores
class MaestroList(generics.ListCreateAPIView):#Creamos una esta clase que mostrará la Lista de Maestros
	queryset = Maestro.objects.all()#
	serializer_class = MaestroSerializer

#Clase que permitirá RECUPERAR, ACTUALIZAR Y DESTRUIR
#VISTA - LISTA DETALLES DE Profesores
class MaestroDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Maestro.objects.all()
	serializer_class = MaestroSerializer	

#VISTA - LISTA DE Alumnos
class AlumnoList(generics.ListCreateAPIView):#Creamos una esta clase que mostrará la Lista de Alumns
	queryset = Alumno.objects.all()#
	serializer_class = AlumnoSerializer

#Clase que permitirá RECUPERAR, ACTUALIZAR Y DESTRUIR
#VISTA - LISTA DETALLES DE Alumnos
class AlumnoDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Alumno.objects.all()
	serializer_class = AlumnoSerializer	

#VISTA - LISTA DE las Clases/Secciones
class ClaseList(generics.ListCreateAPIView):#Creamos una esta clase que mostrará la Lista de Secciones
	queryset = Clase.objects.all()#
	serializer_class = ClaseSerializer

#Clase que permitirá RECUPERAR, ACTUALIZAR Y DESTRUIR
#VISTA - LISTA DETALLES DE Alumnos/Secciones
class ClaseDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Clase.objects.all()
	serializer_class = ClaseSerializer		
#Definimos vistas genéricas (que en realidad ya están creadas)
#Vistas del modulo generics que importamos del rest_framework
#al cual configuramos: 
#1- Los objetos a usar (objetos de deposito)
#2- Los atributos de esos objetos


#Vista de la ventana Home
def home(request):
	titulo = 'Log In'
	ingresode = 'Ingreso de Usuario'
	creator = 'CREATOR'
	form = FormularioRegistro()

	args = {
		'Titulo':titulo,
		'ingresode':ingresode,
		'creator':creator,
		"elFormulario":form,
	}
	return render(request, 'control/login.html', args) #Retornamos para el html indicado los argumentos

def login(request):
	return HttpResponse("BIENVENIDO Al HOME PAGE")
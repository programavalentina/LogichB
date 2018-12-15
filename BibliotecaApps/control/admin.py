
#OOOOOJJJJJJOOOOOOO 
#Se debe importar los modelos creados en el archivo models.py

from django.contrib import admin

from control.models import Administrador, Director, Maestro, Alumno, Clase

class AdminRegistrado(admin.ModelAdmin):
	list_display=["codigo", "nombres", "apellidos", "correo"]
	list_filter = ["nombres"]
	search_fields = ["nombres", "codigo"]

class DirectorRegistrado(admin.ModelAdmin):
	list_display=["codigo", "nombres", "apellidos", "correo", "codigo_admin"]
	list_filter = ["nombres"]
	search_fields = ["nombres", "codigo"]	


class AlumnoRegistrado(admin.ModelAdmin):
	list_display=["codigo", "nombres", "apellidos", "correo", "codigo_clase"]
	list_filter = ["nombres"]
	search_fields = ["nombres", "codigo"]

class MaestroRegistrado(admin.ModelAdmin):
	list_display=["codigo", "nombres", "apellidos", "correo", "curso", "codigo_director"]
	list_filter = ["nombres"]
	search_fields = ["nombres", "codigo"]	

class CursoRegistrado(admin.ModelAdmin):
	list_display=["codigo", "nombre", "descripcion", "codigo_director"]
	list_filter = ["nombre"]
	search_fields = ["nombre", "codigo"]

#Registramos los modelos o Clases creadas en el archivo models.py
#Con esto indicamos que muestre en la base de datos estas tablas
admin.site.register(Administrador, AdminRegistrado)
admin.site.register(Director, DirectorRegistrado)
admin.site.register(Maestro, MaestroRegistrado)
admin.site.register(Alumno, AlumnoRegistrado)
admin.site.register(Clase, CursoRegistrado)



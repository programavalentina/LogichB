from django import forms

class FormularioRegistro(forms.Form):
	nombre = forms.CharField(max_length=100)
	edad = forms.IntegerField()
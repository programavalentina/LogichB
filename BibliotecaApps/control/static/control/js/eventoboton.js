window.onload = function()
{
	document.getElementById('boton').onclick = function()
	{
		var usuario = document.getElementById('nombre').value;
		var contra = document.getElementById('contraseña').value;

		if(usuario=="root@gmail.com" && contra == "0000")
		{
			alert("Usuario y Contraseña correctos.")
		}
		else if(usuario=="" && contra == "")
		{
			alert("Los campos están vacios.")
		}
		else if(usuario=="")
		{
			alert("Debe ingresar un correo.")
		}
		else if(usuario!="root@gmail.com")
		{
			alert("El correo ingresado no es correcto.")
		}		
		else if(contra == "")
		{
			alert("El campo de contraseña está vacio")
		}		
		else if(contra != "0000")
		{
			alert("La contraseña ingresada no es correcta.")
		}
	}
}
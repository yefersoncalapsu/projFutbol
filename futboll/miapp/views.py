from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from .models import*
from .forms import*




#-------------------------------------------------------
# ver elementos de las tablas de la DB
#-------------------------------------------------------

def vista_lista_futbolista(request):
	lista= Futbolista.objects.filter()
	return render(request, 'lista_futbolista.html', locals())

def vista_entrenador(request):
	lista= Entrenador.objects.filter()
	return render(request, 'lista_entrenador.html', locals())


def vista_equipo(request):
	lista= Equipo.objects.filter()
	return render(request, 'lista_equipo.html', locals())

def vista_academia(request):
	lista= Academia.objects.filter()
	return render(request, 'lista_academia.html', locals())

#--------------------------------------------------------------
#  Agregar   elementos a las tablas
#--------------------------------------------------------------
def vista_agregar_futbolista(request):
	if request.method == 'POST':
		formulario = agregar_futbolista_form(request.POST,request.FILES)
		if formulario.is_valid():
			futb = formulario.save(commit =False)
			futb.save()
			formulario.save_m2m()
			return redirect ('/lista_futbolista/')
	else:
		formulario=agregar_futbolista_form()
	return render(request, 'agregar_futbolista.html', locals())

def vista_agregar_entrenador(request):
	if request.method == 'POST':
		formulario = agregar_entrenador_form(request.POST,request.FILES)
		if formulario.is_valid():
			entr = formulario.save(commit =False)
			entr.save()
			formulario.save_m2m()
			return redirect ('/lista_entrenador/')
	else:
		formulario=agregar_entrenador_form()
	return render(request, 'agregar_entrenador.html', locals())

def vista_agregar_equipo(request):
	if request.method == 'POST':
		formulario = agregar_equipo_form(request.POST,request.FILES)
		if formulario.is_valid():
			equi = formulario.save(commit =False)
			equi.save()
			formulario.save_m2m()
			return redirect ('/lista_equipo/')
	else:
		formulario=agregar_equipo_form()
	return render(request, 'agregar_equipo.html', locals())

def vista_agregar_academia(request):
	if request.method == 'POST':
		formulario = agregar_academia_form(request.POST,request.FILES)
		if formulario.is_valid():
			acad = formulario.save(commit =False)
			acad.save()
			formulario.save_m2m()
			return redirect ('/lista_academia/')
	else:
		formulario=agregar_academia_form()
	return render(request, 'agregar_academia.html', locals())
	

#--------------------------------------------------------------
#  ver detalle de los elementos de las tablas
#--------------------------------------------------------------

def vista_ver_futbolista(request, id_futb):
	f = Futbolista.objects.get(id=id_futb)
	return render(request,'ver_futbolista.html',locals())

def vista_ver_entrenador(request, id_entr):
	et = Entrenador.objects.get(id=id_entr)
	return render(request,'ver_entrenador.html',locals())

def vista_ver_equipo(request, id_equi):
	eq = Equipo.objects.get(id=id_equi)
	return render(request,'ver_equipo.html',locals())

def vista_ver_academia(request, id_acad):
	a = Academia.objects.get(id=id_acad)
	return render(request,'ver_academia.html',locals())


#--------------------------------------------------------------
#  editar de los elementos de las tablas
#--------------------------------------------------------------

def vista_editar_futbolista(request, id_futb):
	futb= Futbolista.objects.get(id=id_futb)
	if request.method == "POST":
		formulario = agregar_futbolista_form(request.POST)
		if formulario.is_valid():
			futb = formulario.save()
			return redirect ('/lista_futbolista/')
	else:
		formulario = agregar_futbolista_form(instance=futb)
	return render(request, 'agregar_futbolista.html', locals())

def vista_editar_entrenador(request, id_entr):
	entr= Entrenador.objects.get(id=id_entr)
	if request.method == "POST":
		formulario = agregar_entrenador_form(request.POST)
		if formulario.is_valid():
			entr = formulario.save()
			return redirect ('/lista_entrenador/')
	else:
		formulario = agregar_entrenador_form(instance=entr)
	return render(request, 'agregar_entrenador.html', locals())

def vista_editar_equipo(request, id_equi):
	equi= Equipo.objects.get(id=id_equi)
	if request.method == "POST":
		formulario = agregar_equipo_form(request.POST)
		if formulario.is_valid():
			equi = formulario.save()
			return redirect ('/lista_equipo/')
	else:
		formulario = agregar_equipo_form(instance=equi)
	return render(request, 'agregar_equipo.html', locals())

def vista_editar_academia(request, id_acad):
	acad= Academia.objects.get(id=id_acad)
	if request.method == "POST":
		formulario = agregar_academia_form(request.POST)
		if formulario.is_valid():
			acad = formulario.save()
			return redirect ('/lista_academia/')
	else:
		formulario = agregar_academia_form(instance=acad)
	return render(request, 'agregar_academia.html', locals())

#--------------------------------------------------------------
#  eliminar los elementos de las tablas
#--------------------------------------------------------------


def vista_eliminar_futbolista(request, id_futb):
	futb = Futbolista.objects.get(id=id_futb)
	futb.delete()
	return redirect('/lista_futbolista/')

def vista_eliminar_entrenador(request, id_entr):
	entr = Entrenador.objects.get(id=id_entr)
	entr.delete()
	return redirect('/lista_entrenador/')

def vista_eliminar_equipo(request, id_equi):
	equi = Equipo.objects.get(id=id_equi)
	equi.delete()
	return redirect('/lista_equipo/')

def vista_eliminar_academia(request, id_acad):
	acad = Academia.objects.get(id=id_acad)
	acad.delete()
	return redirect('/lista_academia/')


def vista_login (request):
	usu = ""
	cla = ""
	if request.method == "POST":
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/inicio2/')
			else:
				msj = "usuario o clave incorrectos "
	formulario = login_form()
	return render(request, 'login.html', locals())

def vista_logout (request):
	logout(request)
	return redirect('/login/')



def vista_register(request):
	formulario = register_form()
	if request.method == 'POST':
		formulario = register_form(request.POST)
		if formulario.is_valid():
			usuario = formulario.cleaned_data['username']
			correo 	= formulario.cleaned_data['email']
			password_1 = formulario.cleaned_data['password_1']
			password_2 = formulario.cleaned_data['password_2']
			u = User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()
			return render(request, 'gracias_por_registrarse.html', locals())
		else:
			return render(request, 'register.html', locals())
	return render(request, 'register.html', locals())

##---------------------------------------------
## vista para ver el ws en formato xml
def ws_productos_vistaxml(request):
	data = serializers.serialize('xml', Producto.objects.filter(status=True))
	return HttpResponse(data, content_type='application/xml')

##---------------------------------------------
## vista para ver el ws en formato json
def ws_productos_vistajson(request):
	data = serializers.serialize('json', Producto.objects.filter(status=True))
	return HttpResponse(data, content_type='application/json')

## ---------------------------------------------
##base1 para los templates de register y login
def vista_base1(request):
	return render(request, 'base.html', locals())
##----------------------------------------------
## base2 para los demas templates depues de
## iniciar sesion
def vista_base2(request):
	User.objects.filter()
	return render(request, 'base2.html', locals())

##----------------------------------------------
## template que inicia al ejecutar el puerto
## 127.0.0.1:8000
def vista_inicio_base1(request):
	return render(request, 'inicio1.html', locals())

##-----------------------------------------------
## template al cual es redirigido despues
# de haber iniciado sesion
def vista_inicio_base2(request):
	return render(request, 'inicio2.html', locals())
from django .urls import path
from django.contrib import admin
from .views import*



urlpatterns = [
	#-----------------------------------------------------------------------------
	##listado de consultas bd
	path('lista_futbolista/', vista_lista_futbolista, name='futbolista'),
	path('lista_entrenador/', vista_entrenador, name='entrenador'),
	path('lista_equipo/', vista_equipo, name='equipo'),
	path('lista_academia/', vista_academia, name='academia'),

	#------------------------------------------------------------------------------
	#  url para ver detalle de los elementos
	#------------------------------------------------------------------------------

	path('ver_futbolista/<int:id_futb>/', vista_ver_futbolista, name='ver_futbolista'),
	path('ver_entrenador/<int:id_entr>/', vista_ver_entrenador, name='ver_entrenador'),
	path('ver_equipo/<int:id_equi>/', vista_ver_equipo, name='ver_equipo'),
	path('ver_academia/<int:id_acad>/', vista_ver_academia, name='ver_academia'),

	#------------------------------------------------------------------------------
	#  url para agregar elementos a las tablas
	#------------------------------------------------------------------------------
	path('agregar_futbolista/',vista_agregar_futbolista, name='vista_agregar_futbolista'),
	path('agregar_entrenador/',vista_agregar_entrenador, name='vista_agregar_entrenador'),
	path('agregar_equipo/',vista_agregar_equipo, name='vista_agregar_equipo'),
	path('agregar_academia/',vista_agregar_academia, name='vista_agregar_academia'),


	#------------------------------------------------------------------------------
	#  url para editar elementos a las tablas
	#------------------------------------------------------------------------------
	path('editar_futbolista/<int:id_futb>/', vista_editar_futbolista, name='editar_futbolista'),
	path('editar_entrenador/<int:id_entr>/', vista_editar_entrenador, name='editar_entrenador'),
	path('editar_equipo/<int:id_equi>/', vista_editar_equipo, name='editar_equipo'),
	path('editar_academia/<int:id_acad>/', vista_editar_academia, name='editar_academia'),

	#------------------------------------------------------------------------------
	#  url para eliminar elementos a las tablas
	#------------------------------------------------------------------------------
	path('eliminar_futbolista/<int:id_futb>/', vista_eliminar_futbolista, name='eliminar_futbolista'),
	path('eliminar_entrenador/<int:id_entr>/', vista_eliminar_entrenador, name='eliminar_entrenador'),
	path('eliminar_equipo/<int:id_equi>/', vista_eliminar_equipo, name='eliminar_equipo'),
	path('eliminar_academia/<int:id_acad>/', vista_eliminar_academia, name='eliminar_academia'),
	
	#----------------------------------------------
	# url de login o inicio de sesion
	path('login/', vista_login, name='login'),

	#----------------------------------------------
	# url de log out o cierre de sesion
	path('logout/', vista_logout, name='logout'),
	
	#----------------------------------------------
	# url para el registr de un usuario
	path('register/', vista_register, name='registrar'),

	#--------------------------------------------------------------
	##servisios web
	path('wsxml/productos', ws_productos_vistaxml, name = 'xml'),
	path('wsjson/productos', ws_productos_vistajson, name = 'json'),
	#--------------------------------------------------------------
	# url de templates bases
	path('base1/', vista_base1, name='base1'),
	path('base2/', vista_base2, name='base2'),

	#----------------------------------------------
	# url de templates de inicio en la base1 y base2
	path('', vista_inicio_base1, name='inicio1'),
	path('inicio2/', vista_inicio_base2, name='inicio2'),
	

]
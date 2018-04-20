from django.shortcuts import render
from .serializer import*
from rest_framework import viewsets


class futbolista_viewset(viewsets.ModelViewSet):
	queryset = Futbolista.objects.all()
	serializer_class = futbolista_serializer


class entrenador_viewset(viewsets.ModelViewSet):
	queryset = Entrenador.objects.all()
	serializer_class = entrenador_serializer

class equipo_viewset(viewsets.ModelViewSet):
	queryset = Equipo.objects.all()
	serializer_class = equipo_serializer

class academia_viewset(viewsets.ModelViewSet):
	queryset = Academia.objects.all()
	serializer_class = academia_serializer
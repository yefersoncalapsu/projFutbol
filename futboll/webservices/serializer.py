from rest_framework import serializers
from miapp.models import*

class futbolista_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Futbolista
		fields = ('url','nombre','correo', 'telefono', 'foto', 'equipo', 'academia',)

class entrenador_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Entrenador
		fields = ('url','id', 'nombre','correo', 'telefono',)

class equipo_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Equipo
		fields = ('url','nombre','entrenador',)

class academia_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Academia
		fields = ('url','nombre',)

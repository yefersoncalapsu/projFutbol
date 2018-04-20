from django.urls import path, include
from rest_framework import routers
from miapp.models import*
from webservices.views import*

router = routers.DefaultRouter()
router.register(r'futbolista', futbolista_viewset)
router.register(r'entrenador', entrenador_viewset)
router.register(r'equipo', equipo_viewset)
router.register(r'academia', academia_viewset)


urlpatterns =[
		path('api/', include(router.urls)),
		path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
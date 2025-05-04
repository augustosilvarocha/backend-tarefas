from django.contrib import admin
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/tarefa', TarefaViewSet)

urlpatterns = router.urls

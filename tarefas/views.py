from .models import Tarefa
from .serializers import TarefaSerializers
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

class TarefaViewSet(ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['prioridade']

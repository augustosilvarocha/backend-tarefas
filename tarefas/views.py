from .models import Tarefa
from .serializers import TarefaSerializers
from rest_framework.viewsets import ModelViewSet

class TarefaViewSet(ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializers

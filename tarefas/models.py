from django.db import models


class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('nao_iniciado', 'Não Iniciado'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
    ]
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]
    
    nome = models.CharField(verbose_name="Nome", max_length=100)
    responsavel = models.CharField(verbose_name="Responsavel")
    status = models.CharField(verbose_name="Status", choices=STATUS_CHOICES, default='nao_iniciado')
    prazo = models.DateTimeField(verbose_name="Prazo")
    prioridade = models.CharField(verbose_name="Prioridade", choices=PRIORIDADE_CHOICES, max_length=20, default='media')
    observacao = models.TextField(blank=True, null=True)

    
    def __str__(self):
        return self.nome


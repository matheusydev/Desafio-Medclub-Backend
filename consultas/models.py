from django.db import models

class Consulta(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    nome_medico = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=50)
    localizacao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_medico} - {self.data} às {self.hora}"
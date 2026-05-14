from django.db import models

class Consulta(models.Model):
    data = models.DateTimeField()
    nome_medico = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=50)
    localizacao = models.CharField(max_length=100)



# export type Consulta = {
#   id: string;
#   data: Date;
#   medico: string;
#   especialidade: string;
#   localizacao: string
# };
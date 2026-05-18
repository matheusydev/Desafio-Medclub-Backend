from .models import Consulta
from rest_framework import viewsets
from .serializers import ConsultaSerializer
from drf_spectacular.utils import extend_schema

# Create your views here.
class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    @extend_schema(summary="Lista todas as consultas")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="Cadastra uma nova consulta")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="Retorna detalhes de uma consulta")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="Atualiza uma consulta existente")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="Remove uma consulta")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
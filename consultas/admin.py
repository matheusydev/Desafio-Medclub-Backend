from django.contrib import admin
from .models import Consulta

# Register your models here.

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['nome_medico','data', 'localizacao']
    search_fields = ['nome_medico','data']
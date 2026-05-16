from django.shortcuts import render, redirect
from .models import Consulta

# Create your views here.
def criar_consulta(request):
    if request.method == 'GET':
        return render(request, 'criar_consulta.html')
    elif request.method == 'POST':
        nome_medico = request.POST.get('nome_medico')
        data = request.POST.get('data')
        especialidade = request.POST.get('especialidade')
        localizacao = request.POST.get('localizacao')

        consulta = Consulta(
            nome_medico = nome_medico,
            data = data,
            especialidade = especialidade,
            localizacao = localizacao,
        )
        
        consulta.save()

        return redirect('criar_consulta')
        
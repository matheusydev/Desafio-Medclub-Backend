from django.shortcuts import render

# Create your views here.
def criar_consulta(request):
    return render(request, 'criar_consulta.html')
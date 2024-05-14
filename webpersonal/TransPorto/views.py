from django.shortcuts import render

def pagina_principal(request):
    return render(request, "TransPorto/index.html")


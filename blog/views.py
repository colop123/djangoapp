from django.shortcuts import render

def listar_articulo(request):
    return render(request, 'blog/listar_articulo.html', {})

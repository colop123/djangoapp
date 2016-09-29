from django.shortcuts import render
from django.utils import timezone
from .models import Postear

def listar_articulo(request):
    posts= Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_articulo.html', {'posts': posts})

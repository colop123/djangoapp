from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Postear
from .forms import PostForm
from django.shortcuts import redirect

def listar_articulo(request):
    posts= Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_articulo.html', {'posts': posts})

def detalle_articulo(request, pk):
        post = get_object_or_404(Postear, pk=pk)
        return render(request, 'blog/detalle_articulo.html', {'post': post})

def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.fecha_publicacion = timezone.now()
                post.save()
                return redirect('blog.views.detalle_articulo', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
        post = get_object_or_404(Postear, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('blog.views.detalle_articulo', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

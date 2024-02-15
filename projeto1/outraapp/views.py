from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comentario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST' and request.user.is_authenticated:  
        conteudo = request.POST.get('conteudo')
        comentario = Comentario(nome=request.user.username, email=request.user.email, conteudo=conteudo, post=post)
        comentario.save()
        return redirect('post_detail', slug=post.slug)
    return render(request, 'post_details.html', {'post': post})

def register(request):
    if request.method == 'POST':    
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def create_post(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        autor = request.POST.get('autor') 
        resumo = request.POST.get('resumo') 
        slug = request.POST.get('slug')  
        img_url = request.POST.get('img_url') 
        publicado_em = timezone.now()
        post = Post(titulo=titulo, conteudo=conteudo, autor=autor, resumo=resumo, slug=slug, img_url=img_url, publicado_em=publicado_em)
        post.save()
        return redirect('home')
    return render(request, 'create_post.html')

def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.titulo = request.POST.get('titulo')
        post.conteudo = request.POST.get('conteudo')
        post.autor = request.POST.get('autor')
        post.resumo = request.POST.get('resumo')
        post.slug = request.POST.get('slug')
        post.img_url = request.POST.get('img_url')
        post.save()
        return redirect('home')
    else:
        return render(request, 'edit_post.html', {'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    else:
        return render(request, 'delete_post.html', {'post': post})
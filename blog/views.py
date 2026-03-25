from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .utils import get_news, get_weather, get_gifs


def home(request):
    query = request.GET.get('q')

    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()

    return render(request, 'blog/home.html', {
        'posts': posts.order_by('-created_at'),
        'news': get_news(),
        'weather': get_weather(),
        'gifs': get_gifs(),
        'query': query
    })


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def create_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('home')

    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('post_detail', id=post.id)

    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'blog/delete_confirm.html', {'post': post})


def user_login(request):
    error = None

    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user:
            login(request, user)
            return redirect('home')
        else:
            error = "Invalid credentials"

    return render(request, 'blog/login.html', {'error': error})


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')

    return render(request, 'blog/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
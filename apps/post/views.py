from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.postgres.search import SearchVector
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from django.contrib import messages
from apps.post.models import Post
from .forms import PostForm

def post_list(request):

    form = SearchForm()
    posts = Post.objects.all()
    
    if "search_form" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            posts = Post.available_mamager.annotate(search=SearchVector(
                'title', 'text')).filter(search=query)

    return render(request, 'post/posts.html', {'form': form, "posts": posts})


def post_detail(request, slug):
    post = Post.objects.filter(slug=slug).first()
    if not post:
        messages.add_message(request, messages.SUCCESS, "Post não encontrado")
        return redirect('post:post_list')

    return render(request, "post/post-detail.html", {"post": post})


@login_required
def post_add(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(request, messages.SUCCESS, "Post salvo")
            return redirect("post:post_list")
    return render(request, "post/post-add.html", {"form": form})


@login_required
def post_edit(request, slug):
    
    post = Post.objects.filter(slug=slug).first()
    form = PostForm(request.POST or None,request.FILES or None, instance=post)
    
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect("account:profile-detail-view", slug)
    return render(request, "post/post-add.html", {"form": form})


@login_required
def post_delete(request, slug):
    
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.add_message(request, messages.SUCCESS, "Post removido")
    return redirect("account:profile-detail-view", slug)
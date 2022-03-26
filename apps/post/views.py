from django.shortcuts import render, redirect
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm
from django.contrib import messages
from apps.post.models import Post


def post_list(request):

    form = SearchForm()
    posts = Post.objects.all()
    if "search_form" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            posts = Post.objects.all(search=SearchVector(
                'title', 'text')).filter(search=query)

    return render(request, 'post/posts.html', {'form': form, "posts": posts})


def post_detail(request, slug):

    post = Post.objects.filter(slug=slug).first()

    if not post:
        messages.add_message(request, messages.SUCCESS, "Post não encontrado")
        return redirect('post:post_list')

    return render(request, "post/post-detail.html", {"post": post})

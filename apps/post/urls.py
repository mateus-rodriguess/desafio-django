from unicodedata import name
from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path("add/post", views.post_add, name="post_add"),
    path("edit/post/<slug:slug>", views.post_edit, name="post_edit"),
    path("delete/post/<slug:slug>/",views.post_delete, name="post_delete"),
    path("sobre/", views.about, name="about"),
]

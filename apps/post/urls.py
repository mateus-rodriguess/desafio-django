from unicodedata import name
from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path("post/add", views.post_add, name="post_add"),
    path("post/edit/<slug:slug>", views.post_edit, name="post_edit"),
    path("post/delete/<slug:slug>/",views.post_delete, name="post_delete")
]

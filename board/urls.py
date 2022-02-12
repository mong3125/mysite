from django.contrib import admin
from django.urls import path
from . import views
app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/detail/<int:post_id>/', views.post_detail, name='detail'),
    path('comment/create/<int:post_id>/', views.comment_create, name='comment_create'),
    path('post/modify/<int:post_id>/', views.post_modify, name='post_modify'),
    path('post/delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/detail/<int:post_id>/', views.post_detail, name='detail'),

]
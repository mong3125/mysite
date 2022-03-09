from django.urls import path
from . import views
app_name = 'schedule'

urlpatterns = [
    path('', views.index, name="index"),
    path('todo/delete/<int:todo_id>/', views.todo_delete, name='todo_delete'),
    path('todo/complete/<int:todo_id>/', views.todo_complete, name='todo_complete'),

]
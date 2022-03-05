from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from collections import defaultdict
from .forms import TodoForm


# Create your views here.


def index(request):
    # 로그인 안되있다면 로그인 창으로
    if request.user.is_anonymous:
        return render(request, 'common/login.html')

    # 일정 출력
    todo_list = request.user.todo_set.order_by('deadline').all()
    todo_list_deadline = defaultdict(list)
    for todo in todo_list:
        todo_list_deadline[todo.deadline].append(todo)
    deadline_list = list(todo_list_deadline.keys())

    # 일정 작성
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('schedule:index')
    form = TodoForm()

    return render(request, 'schedule/index.html', {'form': form,
                                                   'todo_list': todo_list,
                                                   'todo_list_deadline': todo_list_deadline,
                                                   'deadline_list': deadline_list})

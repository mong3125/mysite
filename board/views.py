from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return render(request, 'common/login.html')

    # 게시판 글 목록 출력
    post_list = request.user.post_set.order_by('-create_date')
    # 입력 인자
    page = request.GET.get('page', '1')

    #페이징 처리
    paginator = Paginator(post_list, 15)
    page_obj = paginator.get_page(page)
    last_page = len(paginator.page_range)
    context = {'post_list': page_obj, 'last_page' : last_page}

    return render(request, 'board/board.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.author = request.user
            post.feelingWeather = request.POST.get('feelingWeather')
            post.save()
            return redirect('board:index')
    # 게시판 글 작성
    form = PostForm()
    return render(request, 'board/create_post.html', {'form' : form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user.is_anonymous:
        return render(request, 'common/login.html')
    elif request.user != post.author:
        return HttpResponse("잘못된 접근입니다.")
    else:
        context = {'post' : post}
        return render(request, 'board/post_detail.html', context)


def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = Comment(post=post, content=request.POST.get('comment'), create_date=timezone.now())
    comment.author = request.user
    comment.save()
    return redirect('board:detail', post_id=post.id)


def post_modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user.is_anonymous:
        return render(request, 'common/login.html')

    if request.user != post.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('board:detail', post_id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.modify_date = timezone.now()
            post.save()
            return redirect('board:detail', post_id=post_id)
    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'board/create_post.html', context)


def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user != post.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('board:detail', post_id=post_id)

    post.delete()
    return redirect('board:index')


def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)

    comment.delete()
    return redirect('board:detail', post_id=comment.post.id)


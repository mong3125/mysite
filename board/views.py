from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
# Create your views here.

def index(request):
    # 게시판 글 목록 출력
    post_list = Post.objects.order_by('-create_date').filter(author=request.user)
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
            post.save()
            return redirect('board:index')
    # 게시판 글 작성
    form = PostForm()
    return render(request, 'board/create_post.html', {'form' : form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        return HttpResponse("이건 생각했었다 애송아.")
    context = {'post' : post}
    return render(request, 'board/post_detail.html', context)

def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = Comment(post=post, content=request.POST.get('comment'), create_date=timezone.now())
    comment.author = request.user
    comment.save()
    return redirect('board:detail', post_id=post.id)
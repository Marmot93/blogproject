from django.shortcuts import render,get_object_or_404
from .models import Post,Category
import markdown


# 主页
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})

# 详情页
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})

# 跳转到归档的主页
def archives(request, year, month):
    # 更换主页文章列表为按月显示
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'blog/index.html', context={'post_list': post_list})

# 分类页
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})
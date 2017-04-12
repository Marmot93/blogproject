from django.shortcuts import render,get_object_or_404
from .models import Post
import markdown


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',# 扩展
                                     'markdown.extensions.codehilite',# 语法高亮
                                     'markdown.extensions.toc',# 自动生成目录
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})
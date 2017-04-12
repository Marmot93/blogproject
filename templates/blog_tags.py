from .blog.models import Post


# 提取最近5篇文章
def get_recent_posts(num=5):
    return Post.objects.all()[:num]
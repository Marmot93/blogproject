from ..models import Post,Category
from django import template


register = template.Library()
# 提取最近5篇文章,装饰为django注册函数
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]

# 按月归档，三个参数
# Post 的创建时间，month 是精度，order='DESC' 表明降序排列
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

# 分类
@register.simple_tag
def get_categories():
    return Category.objects.all()
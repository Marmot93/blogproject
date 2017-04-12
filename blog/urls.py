from django.conf.urls import url
from . import views

# 正则匹配链接中的字符，调用view中的函数，返回对应链接
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
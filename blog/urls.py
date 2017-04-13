from django.conf.urls import url
from . import views

# 正则匹配链接中的字符，调用view中的函数，返回对应链接
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),# 主页
    url(r'^index.html$', views.index, name='index'),# HOME
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),# 详情页
    # 例如如果用户访问 /archives/2017/3/，那么 archives 视图函数的实际调用为：archives(request, year=2017, month=3)
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),# 归档页
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),# 分类页，用PK值对应分类
]
from django.contrib import admin
from .models import Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['name','email','url','created_time','post']

# 把新增的 PostAdmin 也注册进来
admin.site.register(Comment)


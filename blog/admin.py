from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import AWSBlog

@admin.register(AWSBlog)
class AWSBlogAdmin(ModelAdmin):
    list_display=['id','title','date_of_publish']


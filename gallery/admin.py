from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import AWSGallery
# Register your models here.

@admin.register(AWSGallery)
class AdminAWSGallery(ModelAdmin):
    list_display=('title','image')
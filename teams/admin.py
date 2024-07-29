from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import AWSTeams
# Register your models here.
@admin.register(AWSTeams)
class AdminAWSTeams(ModelAdmin):
    list_display=['name','roles','responsibility']

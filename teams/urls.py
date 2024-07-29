from django.urls import path
from .views import AWSTeamList

app_name='teams'
urlpatterns = [
    path('',AWSTeamList.as_view(),name='teamList')
]

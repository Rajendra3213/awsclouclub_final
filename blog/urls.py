from django.urls import path
from .views import BlogList,BlogDetail
app_name='blog'
urlpatterns = [
    path('',BlogList.as_view(),name='bloglist'),
    path('view/<int:id>',BlogDetail.as_view(),name='blogdetail'),
]

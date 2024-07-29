from django.urls import path
from .views import HomeView,AboutUs

app_name="home"
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('aboutus/',AboutUs.as_view(),name="aboutus")
]

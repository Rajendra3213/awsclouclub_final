from django.urls import path
from .views import MembershipRegister,MembershipLogin,MembershipLogout
app_name="AWSUser"
urlpatterns = [
    path("register/",MembershipRegister.as_view(),name="register"),
    path("login/",MembershipLogin.as_view(),name="login"),
    path("logout/",MembershipLogout.as_view(),name="logout")
]

from django.urls import path
from .views import register_webuser, register_paneladmin,user_login

urlpatterns = [
    path('register/webuser/', register_webuser, name="register_webuser"),
    path('register/paneladmin/', register_paneladmin, name="register_paneladmin"),
    path('login/',user_login , name="login"),
]


from django.urls import path 

from . import views

app_name ="users_app"


urlpatterns = [
    path('registro/', views.UserRegisterView.as_view(),name='user_register'),
    path('login/', views.LoginUser.as_view(),name='user_login'),
    path('logout/', views.LogoutView.as_view(),name='user_logout'),
    path('perfil/', views.PerfilView.as_view(),name='user_perfil'),
]
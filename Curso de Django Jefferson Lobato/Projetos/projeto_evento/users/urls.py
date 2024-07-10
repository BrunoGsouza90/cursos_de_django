from django.urls import path # type: ignore
from django.contrib.auth import views as auth_views # type: ignore
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('perfil/<str:username>/', views.editar_perfil, name='editar_perfil'),
    path('meus_eventos/<str:username>/', views.meus_eventos, name='meus_eventos'),
]

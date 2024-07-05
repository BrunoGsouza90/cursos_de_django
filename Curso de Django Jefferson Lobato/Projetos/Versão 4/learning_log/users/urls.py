from django.urls import path # type: ignore
from django.contrib.auth import views as auth_views # type: ignore
from . import views
from .views import pagina_inicial_protegida

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('pagina_inicial/', views.pagina_inicial_protegida, name='pagina_inicial_protegida'),
]

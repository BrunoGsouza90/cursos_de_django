from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
]

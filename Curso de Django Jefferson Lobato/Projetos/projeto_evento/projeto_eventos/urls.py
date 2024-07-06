from django.urls import path # type: ignore
from . import views # type: ignore

urlpatterns = [
    path('', views.evento, name='evento'),
]

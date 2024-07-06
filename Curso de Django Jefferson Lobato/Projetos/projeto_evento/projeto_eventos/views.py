from django.shortcuts import render # type: ignore

def home(request):
    return render(request,'projeto_eventos/home.html')
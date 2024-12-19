from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    return render(request, "template_app/first.html")

    #return render(request, "template_app/first.html") #render'in index.html'i açması gerekiyor. urls.py'a geldiğinde path'de boş bırakıldığında frist.html'i render'la diyoruz.


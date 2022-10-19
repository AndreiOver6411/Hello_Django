from django.http import HttpResponse # views.py это файл представление, в нем храняться ф-и представленя, говорящие о том что должно произойти по конкретному пути path
from django.shortcuts import render

def about(request):
    return render(request,'about.html',{'greting':'hello'}) #HttpResponse('This is my first page') #мы написали ф-ю, кот-ю хотим привязать к нашему пути (urls.py) в request храниться инфа

def home(request):
    return HttpResponse('This is my home') # Http  отклик
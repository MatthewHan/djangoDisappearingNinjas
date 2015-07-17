# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render # inserted this line
def index(request):
    return render(request, 'ninjas/index.html') # updated this line
def show(request, color):
    if color.lower() == 'red':
        context = {'imgsrc':'raphael.jpg',}
    elif color.lower() == 'blue':
        context = {'imgsrc':'leonardo.jpg',}
    elif color.lower() == 'orange':
        context = {'imgsrc':'michelangelo.jpg',}
    elif color.lower() == 'purple':
        context = {'imgsrc':'donatello.jpg',}
    else:
        context = {'imgsrc':'notapril.jpg',}
    return render(request, 'ninjas/show.html',context)
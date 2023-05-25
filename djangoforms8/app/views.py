from django.shortcuts import render

# Create your views here.

def filter(request):
    d={'data':'hOw ARe yOu'}
    return render(request,'filters.html',d)
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def add(request):
    v1=int(request.POST["num1"])
    v2=int(request.POST["num2"])
    res = v1+v2
     
    return render(request,'result.html',{'result': res})

# Create your views here.

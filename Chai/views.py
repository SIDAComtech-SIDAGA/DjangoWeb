from django.shortcuts import render
from django.http import HttpResponse
from .models import Chai
# Create your views here.

def home(request):
    chai = Chai.objects.all()
    return render(request,'home.html',{'chai':chai})
    # return HttpResponse('<h1>Home Page</h1>')

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def base(request):
    return render(request,"base.html")
def home(request):
    return render(request,"myapp/home.html")
def profile(request):
    name="shanu"
    return render(request,"myapp/profile.html",{'name':name})



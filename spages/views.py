from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    # return HttpResponse("helloworld")
    return render(request, "index.html")

def map(request):
    return render(request, "map.html")

def faq(request):
    return render(request, "faq.html")

def about(request):
    return render(request, "about.html")

def rules(request):
    return render(request, "rules.html")
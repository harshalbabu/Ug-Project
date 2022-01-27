from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    # return HttpResponse("helloworld")
    return render(request, "spages/home_page.html")
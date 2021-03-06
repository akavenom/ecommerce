from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at Contact")

def tracker(request):
    return HttpResponse("We are at Tracker")

def search(request):
    return HttpResponse("We are at Search")

def productView(request):
    return HttpResponse("We are at Product View")

def checkout(request):
    return HttpResponse("We are at Checkout")

def login(request):
    return HttpResponse("We are at Login")

def register(request):
    return HttpResponse("We are at Register")

def cart(request):
    return HttpResponse("We are at Cart")
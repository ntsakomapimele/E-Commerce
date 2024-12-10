from django.shortcuts import render
from .models import Product
# Create your views here.

def homepage(request):
    products = Product.objects.all()

    return render(request, 'home.html', {'products':products})



def About(request):
        return render(request, 'About.html',{})

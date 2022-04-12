from django.shortcuts import render,redirect
from main.models import Category , Product
# Create your views here.

def home(request):
    data = Category.objects.all().order_by('-id')
    product = Product.objects.filter(is_popular=True).order_by('-id')
    return render(request, 'resturant.html', {'data':data,'product':product})
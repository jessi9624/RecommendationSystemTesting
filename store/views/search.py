from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def about(request):
    return render(request, 'about.html')

def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact.html', {'thank': thank})

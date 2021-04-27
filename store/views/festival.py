from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from store.models.category import Category

import pandas as pd
import random
from random import randint
from datetime import date, datetime,timedelta
import numpy as np

def festival(request):
  todaydm= (datetime.now() + timedelta(days=7)).date().strftime("%m/%d")#datetime.now().date().strftime("%m/%d")
  festivals= pd.read_csv('app/festivals.csv')
  category= pd.read_csv('app/ctgryProduct_details.csv')
  ctgryid=[]
  for i in range(0,len(festivals['Festivals'])):
    festivals['Dates'][i]= pd.to_datetime(festivals['Dates'][i]).strftime("%m/%d")
  #print(festivals)
  for i in range(0,len(festivals['Festivals'])):
    if (festivals['Dates'][i]== todaydm):
      print("Special offers and discounts for " , festivals['Festivals'][i]," on every item")
      for i in range(0, len(category['id'])):
          ctgryid.append(category['id'][i])
      l=set(ctgryid)
      ctgryid= list(l)
      #categories = Category.get_all_categories()
      products = Product.get_products_by_id(ctgryid)
      return render(request,'festival.html',{'products':products})
          
        

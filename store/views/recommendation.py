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

import pandas as pd
import random
from random2 import randint
from datetime import date
import numpy as np
from datetime import datetime
from iteration_utilities import duplicates


def recommendation(request):
  #customer1 = Customer.objects.filter(id=request.session.get('customer'))[0]
  customer1 = request.session.get('customer')
  print(customer1)
  
  df= pd.read_csv('C:/Users/Chandan/Downloads/project/project/project/eshopdjango-master/pbrght.csv')
  #print(df)
  df1= df.groupby('id')['prod_brought'].apply(list).reset_index()
  #print(df1)
  pid= pd.read_csv('C:/Users/Chandan/Downloads/project/project/project/eshopdjango-master/Product_details.csv')
  #print(pid)
  df5= pd.read_csv('C:/Users/Chandan/Downloads/project/project/project/eshopdjango-master/ctgryProduct_details.csv')
  #print(df5)
  #########new recmndtn
  df6= pd.read_csv('C:/Users/Chandan/Downloads/project/project/project/eshopdjango-master/pbrght1.csv')
  grppbrght = df6.groupby('c_id')['prod_brought'].apply(list).reset_index()
  #print(grppbrght)
  relation = pd.read_csv('C:/Users/Chandan/Downloads/project/project/project/eshopdjango-master/relation.csv')
  #print(relation)
  for i in range(0,len(relation['name'])):
    relation['dob'][i]= pd.to_datetime(relation['dob'][i]).strftime("%m/%d")
  #print(relation)
  grpprd= df5.groupby('c_id')['name'].apply(list).reset_index()
  #print(grpprd)
  it=[]
  itm=[]
  itm1=[]
  for i in range(0,len(df1['prod_brought'])):
    lst= df1['prod_brought'][i]
    #print(lst)
    item= lst[0]
    #print(item)
    if(len(df1['prod_brought'][i])==1):
      continue
      print(i)
    item1=lst[randint(1,len(df1['prod_brought'][i])-1)]
    #print(item1)
    #print("rule"+ str(i)+":"+item +"->"+item1)
    #store this part in dcitionary
    it.append(str(i))
    itm.append(item)
    itm1.append(item1)
  rule={'id':it,"item":itm,"item1":itm1}
  #print(rule)
  s  = pd.DataFrame(rule)
  #print(s)
  def Merge(dict1, dict2):
      return(dict2.update(dict1))
  prid=[]
  prdnm=[]
  cprid=[]
  cprdnm=[]
  for i in range(0,len(df1['prod_brought'])):
    lst= df1['prod_brought'][i]
    #print(lst)
    item= lst[0]
    #print(item)
    if(len(df1['prod_brought'][i])==1):
      continue
      print(i)
    item1=lst[randint(1,len(df1['prod_brought'][i])-1)]
    #print(item1)
    #print("rule"+ str(i)+":"+item +"->"+item1)
    for i in range(0,len(pid)):
      if(pid['name'][i] ==item1 ):
        prid.append(pid['id'][i])
        prdnm.append(item1)
        
    for i in range(0,len(pid)):
      if(pid['name'][i] ==item):
        cprid.append(pid['id'][i])
        cprdnm.append(item)
  data={'Prod_id':prid,'Prod_name':prdnm}
  data1={'CP_id':cprid,'CP_name':cprdnm}
  Merge(data,data1)
  df3= pd.DataFrame(data1)
  #print(df3)
  #print(data)
  #print(data1)
  lcpnm= list(df3['CP_name'])
  lpnm= list(df3['Prod_name'])

  #i=int(input("id:"))
  #h=df.loc[df['id'] == i, 'prod_brought'].iloc[0]
  #print("product brought is",h)
  #if(h in lcpnm):
  #  k=lcpnm.index(h)
  #  print("the recommended item is",lpnm[k])


  id= customer1#int(input("id:"))
  cbday= pd.read_csv('C:/Users/Chandan/Downloads/project/project/project/eshopdjango-master/custbdayd.csv')
  x=len(cbday['id'])
  from datetime import datetime
  today = datetime.now().date().strftime("%m/%d/%Y")
  todaydm= datetime.now().date().strftime("%m/%d")
  for i in range(0,len(cbday['id'])):
    cbday['birthday'][i]= pd.to_datetime(cbday['birthday'][i]).strftime("%m/%d")
  #print(cbday)

  for i in range(0,len(cbday['id'])):
    if(cbday['birthday'][i]== todaydm):
      #cday={'user_id':cbday['user_id'][i],'birthday':cbday['birthday'][i]}
      #print(cday)
      uid=cbday['id'][i]
      #print(True)
      #print(uid)
      ab=''
      if (id == uid):
          for i in range(0,len(df1['id'])):
            if(df1['id'][i]==uid):
              k=random.choice(df1.loc[df1['id'] == uid, 'prod_brought'].iloc[0])
              #print(k)
          for i in range(0, len(df3['Prod_name'])):
              if(df3['Prod_name'][i] == k):
                  z=df3['Prod_id'][i]
                  #print(df3['Prod_id'][i])
              if(df3['CP_name'][i] == k):
                  z=df3['CP_id'][i]
              #print(df3['CP_id'][i])
          #print(z)

          for i in range(0,len(df5)):
              if (df5['id'][i] == z):
                  cid=df5['c_id'][i]
          #print(cid)
          ctgry=[]
          for i in range(0,len(grppbrght)):
              if(grppbrght['c_id'][i]==cid):
                  ctgry.append(list(duplicates(grppbrght['prod_brought'][i])))
          x=[]
          x=ctgry[0]
          #print(x)
          y1=[]
          for i in range(0, len(df5)):
              for j in range(0,len(x)):
                  if( df5['name'][i] == x[j]):
                      y1.append(df5['id'][i])
          list_set = set(y1)
          y3 = (list(list_set))
          print("recommend products for you is",y3)
          for i in range(0,len(relation['user_id'])):
              if(relation['user_id'][i] == id):
                  #print(relation['dob'][i])
                  if(relation['dob'][i] == todaydm):
                      ccid=relation['c_id'][i]
                      ab=relation['relation'][i]
                      ctgry1=[]
                      for i in range(0,len(grppbrght)):
                          if(grppbrght['c_id'][i]==ccid):
                              ctgry1.append(list(duplicates(grppbrght['prod_brought'][i])))
                      x1=[]
                      x1=ctgry1[0]
                      #print(x)
                      y1=[]
                      for i in range(0, len(df5)):
                          for j in range(0,len(x1)):
                              if( df5['name'][i] == x1[j]):
                                  y1.append(df5['id'][i])
                      #y1.extend(y)
                      list_set = set(y1)
                      y1 = (list(list_set))
                      print("relation rcmd",y1)
                  
                  else:
                    y1=[]
                    print("relation birthday is yet to come")
          #print(y1)
          y2=[]
          y2.extend(y1)
          y2.extend(y3)
          products = Product.get_products_by_id(y2)
          print('Myoutput',products)
          a=ab
          print(a)
          return render(request,'recommendation.html',{'products':products,'a':a})

      elif(cbday['birthday'][i]!= todaydm):
          print("your birthday is yet to come")
          for i in range(0,len(relation['user_id'])):
              if(relation['user_id'][i] == id):
                  print(relation['dob'][i])
                  if(relation['dob'][i] == todaydm):
                      ccid=relation['c_id'][i]
                      ctgry1=[]
                      for i in range(0,len(grppbrght)):
                          if(grppbrght['c_id'][i]==ccid):
                              ctgry1.append(list(duplicates(grppbrght['prod_brought'][i])))
                      #print("category", ctgry1)
                      x1=[]
                      x1=ctgry1[0]
                      #print(x)
                      y1=[]
                      for i in range(0, len(df5)):
                          for j in range(0,len(x1)):
                              if( df5['name'][i] == x1[j]):
                                  y1.append(df5['id'][i])
                      
                      list_set = set(y1)
                      y2 = (list(list_set))
                      print("rcmnd relation",y2)
              
                  else:
                    #y2=[]
                    print("relation birthday is yet to come")
          #print(y1)
          y2=[]

          products = Product.get_products_by_id(y2)
          print('Myoutput',products)
          return render(request,'recommendation.html',{'products':products})

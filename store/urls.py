from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.search import about,contact
from .views.Customer_form import contact1
from .views.recommendation import recommendation
from .views.festival import festival
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from . import views


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('about', about, name="AboutUs"),
    path('contact', contact, name="ContactUs"),
    path('Customer_form', contact1, name="contact1"),
    path('recommendation', recommendation, name="recommendation"),
    path('festival', festival, name="festival"),
    #path('recommendation', recommendation.as_view(), name='recommendation'),
    
]

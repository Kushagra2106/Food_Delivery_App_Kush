#None
#    Of
#      A
#       Kind

from django.shortcuts import render, HttpResponse
from datetime import datetime
from customer.models import ThreeZeroOne, DCC, PC, FM, Ltrs, Tott, ANC


# Create your views here.
def index(request):
    #context={
     #   'variable': 'this is sent'
    #}
    return render(request, 'base.html')
    #return HttpResponse("Homepage")

def about(request):
    return render(request, 'about.html')

def restaurants(request):
    return render(request, 'restaurants.html')

def cart(request):
    return render(request, 'cart.html')

def menu_list(request):
    return render(request, 'menu_list.html')

def rate(request):
    return render(request, 'rate.html')

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    return render(request, 'profile.html')

def order(request):
    return render(request, 'order.html')

def order_confirmation(request):
    return render(request, 'order_confirmation.html')


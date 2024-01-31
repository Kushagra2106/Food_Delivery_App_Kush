#None
#    Of
#      A
#       Kind

from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("restaurant_list", views.restaurants, name='restaurants'),
    path("cart", views.cart, name='cart'),
    path("menu_items", views.menu_list, name='menu_items'),
    path("rating", views.rate, name='rate'),
    path("contact", views.contact, name='contact'),
    path("profile", views.profile, name='profile'),
    path("order", views.order, name='order'),
    path("order_confirmation", views.order_confirmation, name='order_confirmation'),
]


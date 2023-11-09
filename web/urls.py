from django.urls import path
from web import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('services',views.services,name="services"),
    path('products',views.products,name="products"),
    path('LogOut/',views.log_out,name = "Logout" ),
    path('Login/',views.log_in,name = "Login" ),
    path('sign_in/',views.sign_in,name = "signIn" ),
]
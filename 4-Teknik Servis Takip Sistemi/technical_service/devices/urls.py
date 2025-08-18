from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

urlpatterns=[
    path('', views.login_register, name = 'login_register'),
    path('login_register/', views.login_register, name='login_register'),
    path('home/', views.home, name = 'home'),
    path('logout/', views.user_logout, name='logout'),
    path('computer/', views.computer, name = 'computer'),
    path('smart_phone/', views.smart_phone, name='smart_phone'),
    path('smart_watch/', views.smart_watch, name='smart_watch'),
    path('tv/', views.tv, name='tv'),
    path('player_equipment/', views.player_equipment, name='player_equipment'),
    path('tablet/', views.tablet , name='tablet'),
    path('defective_devices/', views.defective_devices, name='defective_devices'),
    path('customer_devices', views.customer_devices, name='customer_devices'),
]
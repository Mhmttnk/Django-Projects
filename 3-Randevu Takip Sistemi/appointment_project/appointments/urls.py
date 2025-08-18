from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path('', views.login_register, name='login_register'),
    path('home/', login_required(views.home), name='home'),
    path('hospital/', login_required(views.add_hospital_appointment), name='add_hospital_appointment'),
    path('sport/', login_required(views.add_sport_appointment), name='add_sport_appointment'),
    path('dental_clinic/', login_required(views.add_dental_appointment), name='add_dental_appointment'),
    path('hairdresser/', login_required(views.add_hairdresser_appointment), name='add_hairdresser_appointment'),
]
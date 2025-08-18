from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('add/', views.add_book, name='add_book'),
    path('delete/', views.delete_book, name='delete_book'),
    path('list/', views.list_book, name='list_book'),
    path('edit<int:id>/', views.edit_book, name='edit_book')
]
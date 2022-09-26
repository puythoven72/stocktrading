from django.urls import path
from . import views

urlpatterns = [
   
    path('<str:pk>',views.test,name='test'),
    path('',views.home,name='home'),
]
from django.urls import path
from . import views

urlpatterns = [
   
    # path('<str:pk>',views.test,name='test'),
   
    # path('<str:sbmtFlag>',views.home,name='home'),
    path('',views.home,name='home'),
    path('success/',views.success,name='success'),
] 
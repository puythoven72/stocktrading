from django.urls import path
from . import views

urlpatterns = [
   
    # path('<str:pk>',views.test,name='test'),
   
    # path('<str:sbmtFlag>',views.home,name='home'),
    path('',views.home,name='home'),
    path('success/',views.success,name='success'),
    path('shareinfo/<symbol>/', views.shareinfo,name='shareinfo'),
    path('history/',views.history,name='history'),
    path('sell_stock/<symbol>/',views.sell_stock,name='sell_stock'),
    
] 
from django.urls import path
from . import views

urlpatterns = [
    path('reset_account/',views.reset_account,name='reset_account'),
    path('',views.home,name='home'),
    path('success/',views.success,name='success'),
    path('shareinfo/<symbol>/', views.shareinfo,name='shareinfo'),
    path('history/',views.history,name='history'),
    path('sell_stock/<symbol>/',views.sell_stock,name='sell_stock'),
    
] 
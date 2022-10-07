from django.contrib import admin
from .models import Stocks
from .models import User
# Register your models here.

admin.site.register(Stocks)
admin.site.register(User)


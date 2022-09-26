from django.db import models

# Create your models here.
class Stocks(models.Model):
    #host
    symbol = models.CharField(max_length=10 )
    quantity = models.IntegerField() 
    value = models.DecimalField(max_digits = 7 , decimal_places = 2, default=0)
    stockbuydate = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.symbol
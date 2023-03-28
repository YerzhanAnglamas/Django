from django.db import models

class Product(models.Model):
    brand = models.CharField(max_length=255)
    model = models.TextField()
    year = models.IntegerField()
    price = models.IntegerField()
    

    def __str__(self) -> str:
        return self.brand
    

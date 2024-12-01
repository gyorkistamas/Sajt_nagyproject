from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Rövid termék leírás")
    price = models.IntegerField(null=False)
    image = models.CharField(default="None", max_length=100)
    stock = models.IntegerField(null=False)
    categoryId = models.IntegerField(null=False)
    def __str__(self):
        return f"""ID: {self.id}\nNAME: {self.name}\nPRICE: {self.price}\nSTOCK: {self.stock}\nCATEGORY: {self.categoryId}\nDESCRIPTION: {self.description}\nIMAGE_PATH: {self.image}\n"""
    
    
class CreateProductQueue(models.Model):
    userid = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(default="Rövid termék leírás")
    price = models.IntegerField(null=False)
    image = models.CharField(default="None", max_length=100)
    stock = models.IntegerField(null=False)
    categoryId = models.IntegerField(null=False)
    status = models.CharField(max_length=15, choices=[("PENDING", "PENDING"), ("ACCEPTED", "ACCEPTED"), ("REJECTED", "REJECTED")], null=True, blank=False, default="PENDING")
    reason = models.TextField(null=True)
    def __str__(self):
        return f"""ID: {self.id}\nUSERID: {self.userid}\nNAME: {self.name}\nPRICE: {self.price}\nSTOCK: {self.stock}\nCATEGORY: {self.categoryId}\nDESCRIPTION: {self.description}\nIMAGE_PATH: {self.image}\n"""
    
class Category(models.Model):
    name = models.CharField(choices=[("magyar", "magyar")], max_length=100)
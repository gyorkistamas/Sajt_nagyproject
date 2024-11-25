from pyexpat import model
from django.db import models
# Create your models here.


    

    
    
class CartModel(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    price = models.IntegerField()
    
class CartItems(models.Model):
    cartId = models.ForeignKey('CartModel', on_delete=models.CASCADE)
    itemId = models.ForeignKey('itemManager.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
#     
# 
# class Payment(models.Model):
#     cartId = models.ForeignKey('Cart', on_delete=models.CASCADE)
#     date = models.DateTimeField()
#     bank_type_hun = models.CharField(choices=[("K&H", "K&H"), ("OTP", "OTP"),
#                                               ("CIB", "CIB"), ("ERSTE", "ERSTE"),
#                                               ("BKS", "BKS"), ("RAIF", "RAIF"),
#                                               ("BNP", "BNP"), ("CITI", "CITI")], max_length=10, null=True)
#     bank_type_etc = models.CharField(max_length=20, null=True)        
#     card_last4 = models.CharField(max_length=4)
#     payment_status = models.CharField(choices=[("PENDING", "PENDING"), ("SUCCESS", "SUCCESS"), ("FAILED", "FAILED")], max_length=10)
#     shipment_status = models.CharField(choices=[("PENDING", "PENDING"), ("SUCCESS", "SUCCESS"), ("FAILED", "FAILED")], max_length=10, null=True)
#     shipment_date = models.DateTimeField(null=True)
#     
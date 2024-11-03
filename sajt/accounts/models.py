from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField

# Create your models here.
class CustomUser(AbstractUser):
    level = models.CharField(default="member", choices=[("member", "member"), ("admin", "admin"), ("developper", "developper"), ("owner", "owner")], editable=True, max_length=20)
    is_active = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_google = models.BooleanField(default=False)
    mfa = models.BooleanField(default=False)
    mfa_secret = models.CharField(max_length=32, null=True, blank=True)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    is_name_modified = models.BooleanField(default=False)    
    
    def has_perm(self, perm, obj=None):
        pass
    
    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.username
    
# class FavouriteItems(models.Model):
#     accountId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     itemId = models.ForeignKey('main.Item', on_delete=models.CASCADE)
#     
#     def __str__(self):
#         return f"{self.accountId}\t{self.itemId}"
#     
# class FavouriteCategories(models.Model):
#     accountId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     categoryId = models.ForeignKey('main.Category', on_delete=models.CASCADE)
#     
#     def __str__(self):
#         return f"{self.accountId}\t{self.categoryId}"
#     
# class Feedbacks(models.Model):
#     accountId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     itemId = models.ForeignKey('main.Item', on_delete=models.CASCADE)
#     message = models.TextField()
#     feedback_stars = models.IntegerField(max_length=1)
#     
#     def __str__(self):
#         return f"{self.accountId}\t{self.message}"
#     
#     
# class city(models.Model):
#     zipcode = models.IntegerField(max_length=6)
#     name = models.CharField(max_length=255)
#     state = models.CharField(choices=[("Bács-Kiskun", "Bács-Kiskun"), ("Baranya", "Baranya"), 
#                                       ("Békés", "Békés"), ("Borsod-Abaúj-Zemplén", "Borsod-Abaúj-Zemplén"),
#                                       ("Fejér", "Fejér"), ("Győr-Moson-Sopron", "Győr-Moson-Sopron"),
#                                       ("Hajdú-Bihar", "Hajdú-Bihar"), ("Heves", "Heves"),
#                                       ("Jász-Nagykun-Szolnok", "Jász-Nagykun-Szolnok"),
#                                       ("Komárom-Esztergom", "Komárom-Esztergom"),
#                                       ("Nógrád", "Nógrád"), ("Pest", "Pest"),
#                                       ("Somogy", "Somogy"), 
#                                       ("Szabolcs-Szatmár-Bereg", "Szabolcs-Szatmár-Bereg"),
#                                       ("Tolna", "Tolna"), ("Vas", "Vas"), ("Veszprém", "Veszprém"),
#                                       ("Zala", "Zala"), ("Veszprém", "Veszprém")], max_length=100)
#     
#     def __str__(self):
#         return self.name
#     
# class saved_Shipment(models.Model):
#     userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     zipcode = models.ForeignKey(city, on_delete=models.CASCADE)
#     street1 = models.CharField(max_length=100)
#     street2 = models.CharField(max_length=100)
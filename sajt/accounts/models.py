from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from datetime import timedelta
from django.utils import timezone
import uuid
from sajt import settings
from session_engine.models import CustomSession
from django.conf import Settings

# Create your models here.
class CustomUser(AbstractUser):
    level = models.CharField(default="member", choices=[("member", "member"), ("admin", "admin"), ("developper", "developper"), ("owner", "owner")], editable=True, max_length=20)
    is_active = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    mfa = models.BooleanField(default=False)
    mfa_secret = models.CharField(max_length=32, null=True, blank=True)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    is_name_modified = models.BooleanField(default=False)   
    phone = models.CharField(max_length=15, null=True, blank=True) 
    selected_shipment = models.ForeignKey('accounts.saved_Shipment', on_delete=models.CASCADE, null=True, blank=True)
    #is_authenticated = models.BooleanField(default=False)
    def has_perm(self, perm, obj=None):
        pass
    
    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.username
    
   # @property   
   # def is_auth(self):
   #     if not self.is_active:
   #         return False
   #     return self.is_auth
   # 
   # @is_auth.setter
   # def is_auth(self, value):
   #     if self.is_active:
   #         self.is_auth = value
   #     else:
   #         self.is_auth = False
    
class PasswordResetToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def is_valid(self):
        return self.created_at >= timezone.now() > timedelta(hours=1)
    
class FavouriteItems(models.Model):
    accountId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    itemId = models.ForeignKey('itemManager.Product', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.accountId}\t{self.itemId}"
    
class FavouriteCategories(models.Model):
    accountId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoryId = models.ForeignKey('itemManager.Category', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.accountId}\t{self.categoryId}"
    
class Feedbacks(models.Model):
    accountId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    itemId = models.ForeignKey('itemManager.Product', on_delete=models.CASCADE)
    message = models.TextField()
    feedback_stars = models.IntegerField()
    
    def __str__(self):
        return f"{self.accountId}\t{self.message}"
    
    
class city(models.Model):
    zipcode = models.IntegerField()
    name = models.CharField(max_length=255)
    state = models.CharField(choices=[("Bács-Kiskun", "Bács-Kiskun"), ("Baranya", "Baranya"), 
                                      ("Békés", "Békés"), ("Borsod-Abaúj-Zemplén", "Borsod-Abaúj-Zemplén"),
                                      ("Fejér", "Fejér"), ("Győr-Moson-Sopron", "Győr-Moson-Sopron"),
                                      ("Hajdú-Bihar", "Hajdú-Bihar"), ("Heves", "Heves"),
                                      ("Jász-Nagykun-Szolnok", "Jász-Nagykun-Szolnok"),
                                      ("Komárom-Esztergom", "Komárom-Esztergom"),
                                      ("Nógrád", "Nógrád"), ("Pest", "Pest"),
                                      ("Somogy", "Somogy"), 
                                      ("Szabolcs-Szatmár-Bereg", "Szabolcs-Szatmár-Bereg"),
                                      ("Tolna", "Tolna"), ("Vas", "Vas"), ("Veszprém", "Veszprém"),
                                      ("Zala", "Zala"), ("Veszprém", "Veszprém")], max_length=100)
    
    def __str__(self):
        return self.name
    
class saved_Shipment(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    zipcode = models.ForeignKey(city, on_delete=models.CASCADE)
    street1 = models.CharField(max_length=100)
    street2 = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.userId}\t{self.id}"
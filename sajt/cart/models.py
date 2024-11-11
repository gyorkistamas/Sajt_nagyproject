from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Rövid termék leírás")
    price = models.IntegerField(null=False)
    image = models.ImageField(upload_to='images', null=True)
    stock = models.IntegerField(null=False)
    categoryId = models.IntegerField(null=False)
    def __str__(self):
        return f"""ID: {self.id}\nNAME: {self.name}\nPRICE: {self.price}\nSTOCK: {self.stock}\nCATEGORY: {self.categoryId}\nDESCRIPTION: {self.description}\nIMAGE_PATH: {self.image}\n"""
from django.db import models

# Create your models here.
class Translation(models.Model):
    lang_code = models.CharField(max_length=10)
    key = models.CharField(max_length=255, unique=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.lang_code} ({self.key})"
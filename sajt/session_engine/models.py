import django
from django.db import models
import uuid
from datetime import timedelta
from django.utils.timezone import now
from sajt import settings

class CustomSession(models.Model):
    session_key = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sessions")
    session_data = models.JSONField(default=dict)
    last_active = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField(default=now() + timedelta(days=7))
    
    def is_expired(self):
        return now() > self.expire_at
    
    def save(self, *args, **kwargs):
        if not self.expire_at:
            self.expire_at = now() + timedelta(days=7)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Session for {self.user.username} (Expires: {self.expire_at})"

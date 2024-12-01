from session_engine.models import CustomSession
from django.utils.timezone import now

def cleanup_expired_sessions():
    expired_sessions = CustomSession.objects.filter(expire_at__lte=now())
    count = expired_sessions.count()
    expired_sessions.delete()
    return f"Deleted {count} expired sessions"
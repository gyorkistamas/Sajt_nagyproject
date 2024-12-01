from .models import CustomSession
from django.utils.timezone import now
from datetime import timedelta

def create_session(user, session_data=None, expiry_time=7):
    if session_data is None:
        session_data = {}
    session = CustomSession.objects.create(user=user, session_data=session_data, expire_at=now() + timedelta(days=expiry_time))
    return session.session_key

def get_session(session_key):
    try:
        session = CustomSession.objects.get(session_key=session_key)
        if session.is_expired():
            session.delete()
            return None
        return session
    except CustomSession.DoesNotExist:
        return None
    
def cleanup_expired_sessions():
    CustomSession.objects.filter(expire_at__lte=now()).delete()
    
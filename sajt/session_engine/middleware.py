from django.utils.functional import SimpleLazyObject
from session_engine.models import CustomSession
from session_engine.utils import get_session
from django.utils.timezone import now
from django.contrib.auth import get_user_model
class SessionEngineMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session_key = request.COOKIES.get('session_key')
        if session_key:
            session = get_session(session_key=session_key)
            if session:
                request.user = session.user
                request.session_data = session.session_data
            else:
                request.user = None
                request.session_data = None
        CustomSession.objects.filter(expire_at__lt=now()).delete()
        return self.get_response(request)
   
   
User = get_user_model()
def get_user_from_session(session_key):
    try:
        session =CustomSession.objects.get(session_key=session_key)
        if not session.is_expired():
            return session.user
    except CustomSession.DoesNotExist:
        return None
    
class CustomSessionAuthenticationMiddleware:
    def __init__(self, get_respo):
        self.get_respo = get_respo

    def __call__(self, request):
        session_key = request.COOKIES.get('session_key')
        request.user = SimpleLazyObject(lambda: get_user_from_session(session_key))
        return self.get_respo(request)
from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added, pre_social_login
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model

User = get_user_model()

def set_is_google_on_reg(request, sociallogin, **kwargs):
    if sociallogin.account.provider == 'google':
        user = sociallogin.user
        user.is_google = True
        user.save()
        return
    
def set_is_google_on_log(request, sociallogin, **kwargs):
    if sociallogin.account.provider == 'google':
        user = sociallogin.user
        user.is_google = True
        user.save()
        return
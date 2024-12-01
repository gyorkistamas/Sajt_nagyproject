from django.core.cache import cache
from .models import Translation
from django.utils.translation import gettext as _

CACHE_TIMEOUT = 3600

def get_translation(key, lang_code='en'):
    cache_key = f"translation_{lang_code}_{key}"
    translation = cache.get(cache_key)
    
    if not translation:
        try:
            translation_obj = Translation.objects.get(key=key, lang_code=lang_code)
            translation = translation_obj.text
            cache.set(cache_key, translation, CACHE_TIMEOUT)
        except Translation.DoesNotExist:
            translation = _(key)
            cache.set(cache_key, translation, CACHE_TIMEOUT)
            
    return translation
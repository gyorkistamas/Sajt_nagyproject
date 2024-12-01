from multiprocessing.reduction import register
from django import template
from K_localization_framework.translation_loader import get_translation
from django.utils.translation import get_language as lang

register = template.Library()

@register.simple_tag
def translate(key):
    lang_code = lang()
    return get_translation(key, lang_code)
from django.contrib import admin
from .models import Translation

@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('lang_code', 'key', 'text')
    search_field = ('key', 'lang_code')
    list_filter = ('lang_code',)
# Register your models here.

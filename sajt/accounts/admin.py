from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']
    list_filter = ['level']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('level', 'dark_mode', 'is_google', 'mfa', 'mfa_secret', 'last_login_ip')}),
    )
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True
    
admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.

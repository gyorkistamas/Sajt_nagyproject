from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import CustomUser, PasswordResetToken
from django.urls import reverse
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    error = False
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        
        try:
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error = True
                messages.error(request, "Helytelen jelszó")
                return render(request, 'login.html', {"error": error})
        except:
            error = True
            messages.error(request, f"Nincs ilyen felhasználó")
            render(request, 'login.html', {"error": error})
    return render(request, 'login.html', {"error": error})
# Create your views here.

def login_cancelled(request):
    return redirect('/')

def reg_view(request):
    error = False
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pwd")
        confirm_password = request.POST.get("pwd-confirm")
        if not password == confirm_password:
            messages.error(request, "Jelszavak nem egyeznek meg!")
            error = True
            return render(request, 'reg.html', {"error":error})
        if not len(password) >= 8:
            messages.error(request, "Jelszónak legalább 8 karakternek kell lennie!")
            error = True
            return render(request, 'reg.html', {"error":error})
        if not (("@" and ".") in email):
            messages.error(request, "Nem valós email!")
            error = True
            return render(request, 'reg.html', {"error":error})
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Már létezik felhasználó ilyen néven!")
            error = True
            return render(request, 'reg.html', {"error":error})
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Már létezik felhasználó ilyen email címmel!")
            error = True
            return render(request, 'reg.html', {"error":error})
        
        try:
            CustomUser.objects.create_user(username=username, email=email, password=password, date_joined=timezone.now(), level="member", is_active=True, is_staff=False, is_superuser=False, first_name="", last_name="", dark_mode=False, last_login_ip=get_client_ip(request), mfa=False, mfa_secret="", is_name_modified=False)
            messages.success(request, "Sikeres regisztráció")
            return redirect('login')
        except:
            messages.error(request, "Nem sikerult regisztrálni")
            error = True
            return render(request, "reg.html", {"error":error})
    return render(request, 'reg.html', {"error":error})

def lost_pwd_view(request):
    error = False
    success = False
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        if not email and not username:
            user = CustomUser.objects.get(username=username)
            if not username == user.username and not email == user.email:                
                messages.error(request, "Nincs ilyen felhasználó")
                error = True
                return render(request, 'forgot_password.html', {"error":error, "success":success})
        try:
            user = CustomUser.objects.get(email=email)
            reset_token = PasswordResetToken.objects.create(user=user)
            reset_link = request.build_absolute_uri(
                reverse('reset_password') + '?token=' + str(reset_token.token)
            )
            
            send_mail(
                "Password Reset Requested",
                f"Click the link to reset your password: {reset_link}",
                "no-reply@localhost.com",
                [email],
                fail_silently=False,
            )
            messages.success(request, "Password reset sent successfully")
            success = True
            return render(request, 'forgot_password.html', {"error":error, "success":success})
        except:
            messages.error(request, f"Nincs ilyen felhasználó us:{username} email:{email}")
            error = True
            return render(request, 'forgot_password.html', {"error":error, "success":success})
    return render(request, 'forgot_password.html', {"error":error, "success":success})
            
def reset_pwd_view(request):
    token_value = request.POST.get("token")
    try:
        reset_token = PasswordResetToken.objects.get(token=token_value)
        
        if not reset_token.is_valid():
            messages.error(request, "Password reset link has expired")
            return redirect('login/lost+password')
        
        if request.method == "POST":
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            if password != confirm_password:
                messages.error(request, "Passwords do not match")
                return redirect('login/lost+password')
            reset_token.user.password = make_password(password)
            reset_token.user.save()
            reset_token.delete()
            messages.success(request, "Password reset successful")
            return redirect('login/')
        return render(request, 'reset_password.html', {"token":token_value})
    except:
        messages.error(request, "Password reset link has expired")
        return redirect('login/lost+password')
            
            
                
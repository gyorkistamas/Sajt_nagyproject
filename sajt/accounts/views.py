from calendar import isleap
from email import message
from re import U
from urllib import response
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from session_engine.models import CustomSession
from .models import CustomUser, PasswordResetToken, saved_Shipment
from django.urls import reverse
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from session_engine.utils import create_session, get_session

def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

def logout_view(request):
    session_key = request.COOKIES.get('session_key')
    if session_key:
        CustomSession.objects.filter(session_key=session_key).delete()
        
    respo = redirect('/')
    respo.delete_cookie('session_key')
    
    logout(request)
    return respo

def login_view(request):
    error = False
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        
        try:
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                _user = CustomUser.objects.get(username=username)
                _user.is_auth = True
                _user.save()
                session_key = create_session(user)
                respo = redirect('/')
                respo.set_cookie('session_key', session_key, httponly=True, secure=True)                
                messages.success(request, "Sikeres bejelentkezés")
                return respo
            else:
                error = True
                messages.error(request, f"Helytelen jelszó ")
                return render(request, 'login.html', {"error": error})
        except Exception as e:
            error = True
            messages.error(request, f"Nincs ilyen felhasználó   EXCEPTION:{e}")
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
            messages.error(request, "Nem megfelelő email formátum!")
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
            newUser = CustomUser.objects.create_user(username=username, email=email, password=password, date_joined=timezone.now(), level="member", is_active=True, is_staff=False, is_superuser=False, first_name="", last_name="", dark_mode=False, last_login_ip=get_client_ip(request), mfa=False, mfa_secret="", is_name_modified=False, is_auth=True, phone="")
            messages.success(request, "Sikeres regisztráció")
            session_key = create_session(newUser)
            respo = redirect('/')
            respo.set_cookie('session_key', session_key, httponly=True, secure=True)
            newUser.is_authenticated = True
            newUser.save()
            return respo
        except Exception as e:
            messages.error(request, "Nem sikerult regisztrálni")
            error = True
            print(f"Sikertelen regisztráció: {e}")
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
            messages.error(request, f"Nincs ilyen felhasználó ")
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
            
@login_required
def profile(request):
    account = CustomUser.objects.get(email=request.user.email)
    address = saved_Shipment.objects.filter(userId=account.id)
    isAdmin = account.level == "admin" or account.level == "developper" or account.level == "owner"
    data = {
        "username": account.username.capitalize(),
        "email": account.email,
        "phone": account.phone,
        "shipment": address,
        "selected_shipment": account.selected_shipment
    }
    if isAdmin:
        data["perms"] = account.level
    return render(request, 'profile2.html', {"isAdmin":isAdmin, "userData":data })

@login_required
def edit_profile(request):
    account = CustomUser.objects.get(email=request.user.email)
    address = saved_Shipment.objects.filter(userId=account.id)
    isAdmin = account.level == "admin"
    data = {
        "username": account.username.capitalize(),
        "email": account.email,
        "phone": account.phone,
        "shipment": address,
        "selected_shipment": account.selected_shipment
    }
    return render(request, 'profile2.html', {"isAdmin":isAdmin, "userData":data })


@login_required
def admin(request):
    if request.user.level == "member":
        return redirect("/")
    t_users = CustomUser.objects.all()
    userData = {}
    for user in t_users:
        userData[user.id] = {
            "username": user.username
            ,"level": user.level
            ,"first_name": user.first_name.capitalize()
            ,"last_name": user.last_name.capitalize()
            ,"email": user.email
            ,"phone": user.phone
            ,"last_login": user.last_login
            ,"date_joined": user.date_joined
            ,"is_active": user.is_active
            ,"is_staff": user.is_staff
            ,"mfa": user.mfa
            ,"is_name_modified": user.is_name_modified
            ,"last_login_ip": user.last_login_ip
            ,"last_login_location": "Not implemented" # TODO: get last login location                    
        }
    return render(request, 'admin/admin_user_list.html', {"users": userData })

@login_required
def admin_change_email(request, email):
    if request.user.level == "member":
        return redirect("/")
    user = CustomUser.objects.get(email=email)
    new_email = request.POST.get("new_email")
    if new_email:
        if CustomUser.objects.filter(email=new_email).exists():
            messages.error(request, "Már létezik felhasználó ilyen email címmel!")
        else:
            if '@' and '.' in new_email:
                user.email = new_email
                user.save()
                messages.success(request, "Sikeres email módosítás!")
            else:
                messages.error(request, "Nem valós email!")
    else:
        messages.error(request, "Nem valós email!")
    # TODO: send email about the change    
    return redirect('admin')

@login_required
def admin_change_saveUser(request, userId, isLooped=False):
    if request.user.level == "member":
        return redirect("/")
    global isChanged
    isChanged = False
    if request.method == "POST":
        user = CustomUser.objects.get(id=userId)
        try:
            if request.user.id == user.id:
                messages.error(request, "Nem szerkesztheted a saját felhasználódat!")
                if not isLooped:
                    return redirect('admin')
                else:
                    return False
            if  not user.email == request.POST.get("new_email"):
                user.email = request.POST.get("new_email")
                isChanged = True
            if not user.is_name_modified == request.POST.get("is_name_modified"):
                user.is_name_modified = request.POST.get("is_name_modified") == "on"
                isChanged = True
            if not user.first_name == request.POST.get("first_name"):
                user.first_name = request.POST.get("first_name")
                isChanged = True
            if not user.last_name == request.POST.get("last_name"):
                user.last_name = request.POST.get("last_name")
                isChanged = True
            # if not user.phone == request.POST.get("phone"):
            #     user.phone = request.POST.get("phone")

            if request.user.level == "admin" or request.user.level == "owner":
                if not user.level == request.POST.get("level"):
                    user.level = request.POST.get("level")
                    isChanged = True
                if not user.mfa == request.POST.get("mfa"):
                    user.mfa = request.POST.get("mfa") == "on"
                    isChanged = True
            if user.level == "admin" or user.level == "owner" or user.level == "developper":
                user.is_staff = True   
                isChanged = True
            user.save()
            messages.success(request, f"Sikeres módosítás!{request.user.level}/{user.level}")
            if not isLooped:
                return redirect('admin')
            else:
                return True
        except Exception as e:
            messages.error(request, e)
            messages.error(request, f"ID: {userId}/{user.id}\tusername: {user.username}\tlevel: {request.user.level}/{user.level}")
            if not isLooped:
                return redirect('admin')
            else:
                return False
        
    else:
        messages.error(request, f"valami baj van\nID: {userId}")
        if not isLooped:
            return redirect('admin')
        else:
            return False
        

@login_required
def admin_change_saveUsers(request):
    if not request.user.is_staff:
        return redirect("/")
    updated, error = 0, 0
    all_users = CustomUser.objects.all()
    for user in all_users:
        if admin_change_saveUser(request, user.id, True):
            updated += 1
        else:
            error += 1
    if updated == 0 and error == 0:
        messages.error(request, "Nem történtek módosítások!")
    elif (updated == 1 or updated == 0) and (error == 0 or error == 1):
        messages.success(request, f"Sikeres módosítás: {updated}\tHiba: {error}")
    elif updated > 1 and (error == 0 or error == 1):
        messages.success(request, f"Sikeres módosítások: {updated}\tHiba: {error}")
    elif (updated == 0 or updated == 1) and error > 1:
        messages.success(request, f"Sikeres módosítás: {updated}\tHibák: {error}")
    elif updated > 1 and error > 1:
        messages.success(request, f"Sikeres módosítások: {updated}\tHibák: {error}")
    else:
        messages.error(request, f"Ismeretlen hiba történt")
    return redirect('admin')

@login_required
def admin_change_deleteUser(request, userId):
    if not request.user.is_staff:
        return redirect("/")
    if userId != request.user.id:
        try:
            user = CustomUser.objects.get(id=userId)
            if user.level == "member":
                user.delete()
            elif request.level == "admin" or request.level == "owner":
                user.delete()
            else:
                messages.error(request, "Nem törölhetsz staff felhasználót a jelenlegi jogosultságoddal!")
            messages.success(request, f"Felhasználó sikeresen törölve!")
            return redirect('admin')
        except Exception as e:
            messages.error(request, e)
            messages.error(request, f"ID: {userId}")
            return redirect('admin')
    else:
        messages.error(request, f"Nem törölheted a saját felhasználódat!")
        
@login_required
def admin_change_disableUser(request, userId):
    if not request.user.is_staff:
        return redirect("/")
    if userId != request.user.id:
        try:
            user = CustomUser.objects.get(id=userId)
            if user.level == "member":
                user.is_active = False
                user.is_auth = False
                user.save()
                
            elif request.level == "admin" or request.level == "owner":
                user.is_active = False
                user.is_auth = False
                user.save()
                
            else:
                messages.error(request, "Nem tilthatsz staff felhasználót a jelenlegi jogosultságoddal!")
            
            
            messages.success(request, f"Felhasználó sikeresen letiltva!")
            return redirect('admin')
        except Exception as e:
            print(e)
            messages.error(request, e)
            messages.error(request, f"ID: {userId}")
            return redirect('admin')
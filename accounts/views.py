from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm # foydalauvchilarni ro'yxatdan o'tkazish uchun tayyor formadan ham foydalanishimiz mumkin
from .mixin import Mixin
from .forms import LoginForm, UserRegisterFrom, ProfileEditForm
# Create your views here.

class Login(View):
    def get(self, request):
        form = LoginForm()
        context = {
            "form":form,
        }
        return render(request, 'accounts/login.html', context=context)
    def post(self, request):
        form = LoginForm(data=request.POST)
        context = {
            "   form": form,
        }
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password) # username mi username ga, passworddi passwordga teng user topilsa
            if user is not None:
                form = login(request, user)
                messages.success(request, "Muvaffaqiyatli login qildingiz!")
                return redirect('home_page')
            else:
                messages.info(request, "username yoki parolda xatolik bor!")
                return render(request, 'accounts/login.html', context=context)
        else:
            return render(request, 'accounts/login.html', context=context)
class Logout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "Siz logout qildingiz!!")
        return redirect('home_page')

class Profile(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'accounts/user_profile.html')

class RegisterView(View):
    def get(self, request):
        form = UserRegisterFrom()
        context = {
            "form":form,
        }
        return render(request, 'accounts/register.html', context=context)
    def post(self, request):
        form = UserRegisterFrom(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tdingiz!")
            return redirect('login')
        else:
            context = {
                "form": form,
            }
            return render(request, 'accounts/register.html', context=context)

class ProfileEditView(LoginRequiredMixin,View):
    def get(self, request):
        form = ProfileEditForm(instance=request.user)
        context = {
            "form":form,
        }
        return render(request, 'accounts/profile_edit.html', context=context)
    def post(self, request):
        form = ProfileEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil muvaffaqiyatli tahrirlandi!")
            return redirect('user_profile')
        else:
            context = {
                "form":form,
            }
            return render(request, 'accounts/profile_edit.html', context=context)

class AdminPageView(Mixin,View):
    def get(self, request):
        super_users = User.objects.filter(is_superuser=True)
        context = {
            "super_users":super_users,
        }
        return render(request, 'accounts/admin.html', context=context)
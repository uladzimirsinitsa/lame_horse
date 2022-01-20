from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.shortcuts import redirect
from .models import Profile
from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetDoneView
from django.views.generic import RedirectView
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required

UserModel = get_user_model()


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main_en')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login_en.html', {'form': form})


def register_ru(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('main', permanent=True)
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def register_en(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('main_en', permanent=True)
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register_en.html', {'user_form': user_form})


@login_required
def edit_ru(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль обновлен')
        else:
            messages.error(request, 'Ошибка обновления профиля')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def edit_en(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'OK')
        else:
            messages.error(request, 'ERROR')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit_en.html', {'user_form': user_form, 'profile_form': profile_form})


class LogoutViewRu(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutViewRu, self).get(request, *args, **kwargs)


class LogoutViewEn(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutViewEn, self).get(request, *args, **kwargs)


class MyLoginView(LoginView):
    template_name = 'registration/login_en.html'


class ResetViewEn(PasswordResetView):
    template_name = 'registration/password_reset_form_en.html'
    success_url = '/en/account/password_reset/done'


class PasswordResetDoneEn(PasswordResetDoneView):
    template_name = 'registration/password_reset_done_en.html'

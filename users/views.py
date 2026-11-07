from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CustomRegisterForm, CustomAuthLoginForm, VerifyCodeForm
from .models import CustomUser


def send_verification_code(user):
    code = user.generate_code()
    send_mail(
        subject="Код подтверждения регистрации — Library.kg",
        message=(
            f"Здравствуйте, {user.first_name}!\n\n"
            f"Ваш код подтверждения: {code}\n"
            f"Код действует {CustomUser.CODE_LIFETIME_MINUTES} минут.\n\n"
            f"Если вы не регистрировались на Library.kg, просто проигнорируйте это письмо."
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )


# РЕГИСТРАЦИЯ: аккаунт создаётся неактивным, на почту уходит код
def register_view(request):
    if request.method == "POST":
        # убираем старые неподтверждённые попытки с тем же логином/почтой
        CustomUser.objects.filter(is_active=False, is_verified=False).filter(
            Q(username=request.POST.get('username', '')) |
            Q(email__iexact=request.POST.get('email', ''))
        ).delete()

        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False          # войти нельзя, пока не введён код
            user.save()
            send_verification_code(user)
            request.session['verify_user_id'] = user.id
            messages.info(request, f"Мы отправили код на {user.email}")
            return redirect('verify')
    else:
        form = CustomRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# ПОДТВЕРЖДЕНИЕ КОДА: только после этого регистрация завершена
def verify_view(request):
    user_id = request.session.get('verify_user_id')
    if not user_id:
        return redirect('register')
    user = get_object_or_404(CustomUser, id=user_id, is_active=False)

    if request.method == "POST":
        form = VerifyCodeForm(request.POST)
        if form.is_valid():
            if user.code_is_expired():
                form.add_error('code', "Срок действия кода истёк. Отправьте новый код.")
            elif form.cleaned_data['code'] != user.verification_code:
                form.add_error('code', "Неверный код.")
            else:
                user.is_active = True
                user.is_verified = True
                user.verification_code = ''
                user.save()
                del request.session['verify_user_id']
                messages.success(request, "Почта подтверждена! Теперь войдите в аккаунт.")
                return redirect('login')
    else:
        form = VerifyCodeForm()
    return render(request, 'users/verify.html', {'form': form, 'email': user.email})


def resend_code_view(request):
    user_id = request.session.get('verify_user_id')
    if request.method == "POST" and user_id:
        user = get_object_or_404(CustomUser, id=user_id, is_active=False)
        send_verification_code(user)
        messages.info(request, "Новый код отправлен.")
    return redirect('verify')


# АВТОРИЗАЦИЯ с капчей
def auth_login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        form = CustomAuthLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('profile')
    else:
        form = CustomAuthLoginForm(request)
    return render(request, 'users/login.html', {'form': form})


def auth_logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect('login')


# ЛИЧНЫЙ КАБИНЕТ
@login_required
def profile_view(request):
    profile = CustomUser.objects.filter(id=request.user.id).first()
    return render(request, 'users/profile.html', {'profile': profile})

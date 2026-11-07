from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import CustomUser


# Авторизация с капчей
class CustomAuthLoginForm(AuthenticationForm):
    captcha = CaptchaField(label='Подтвердите, что вы не робот')


# Регистрация: 11 полей
class CustomRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True, label="Имя")
    last_name = forms.CharField(max_length=150, required=True, label="Фамилия")
    email = forms.EmailField(required=True, label="Email")
    photo = forms.ImageField(required=True, label="Фото")
    phone_number = forms.CharField(max_length=15, required=True, initial='+996', label="Телефон")
    date_bir = forms.DateField(required=True, label="Дата рождения",
                               widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=CustomUser.GENDER, required=True, label="Пол")
    city = forms.CharField(max_length=100, required=True, label="Город")

    class Meta:
        model = CustomUser
        fields = (
            'username', 'first_name', 'last_name', 'email', 'photo',
            'phone_number', 'date_bir', 'gender', 'city',
            'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError("Пользователь с такой почтой уже зарегистрирован.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# Ввод кода из письма
class VerifyCodeForm(forms.Form):
    code = forms.CharField(
        max_length=6, min_length=6, label="Код из письма",
        widget=forms.TextInput(attrs={'placeholder': '123456', 'autocomplete': 'one-time-code',
                                      'inputmode': 'numeric'}),
    )

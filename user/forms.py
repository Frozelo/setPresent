from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "input-symbol input-symbol1",
                "placeholder": "Имя",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "input-symbol input-symbol2",
                "placeholder": "Фамилия",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "input-symbol input-email",
                "placeholder": "Email",
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "input-symbol",
                    "placeholder": "Номер телефона",
                }
            ),
            "password1": forms.PasswordInput(
                attrs={
                    "class": "input-symbol input-symbol3",
                    "placeholder": "Пароль",
                }
            ),
            "password2": forms.PasswordInput(
                attrs={
                    "class": "input-symbol",
                    "placeholder": "Повторите пароль",
                }
            ),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-symbol",
                "placeholder": "Номер телефона",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input-symbol",
                "placeholder": "Пароль",
            }
        )
    )

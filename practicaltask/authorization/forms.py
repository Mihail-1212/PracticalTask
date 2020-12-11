from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django import forms

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form-control',
        'placeholder': 'Логин',
        'id': 'inputLogin',
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Пароль',
            'id': 'inputPassword',
        }))
    error_messages = {
        'invalid_login': _(
            "Вход в Ежедневник недопустим"
        ),
        'inactive': _("This account is inactive."),
    }

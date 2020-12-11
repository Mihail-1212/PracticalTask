from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

from . import forms

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False), name='authorization_index'),
    path('login/', auth_views.LoginView.as_view(
        authentication_form=forms.UserLoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

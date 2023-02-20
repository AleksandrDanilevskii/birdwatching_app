from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from users.forms import RegistrationForm, LoginForm


class RegistrationView(CreateView):
    model = User
    # fields = ('username', 'email', 'first_name', 'last_name', 'password')
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'users/user_form.html'


class UserLoginView(LoginView):
    template_name = 'users/login_form.html'
    form_class = LoginForm


class UserLogoutView(LogoutView):
    pass

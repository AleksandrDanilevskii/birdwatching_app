from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView

from users.forms import RegistrationForm, LoginForm


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'users/user_form.html'


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login_form.html'


class UserLogoutView(LogoutView):
    pass


class UserTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.request.user
        return context




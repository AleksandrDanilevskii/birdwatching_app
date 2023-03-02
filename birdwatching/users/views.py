from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView

from users.forms import RegistrationForm, LoginForm, UserModelForm


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


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'users/user_edit_form.html'
    form_class = UserModelForm
    success_url = '/users/my-account/'

    def test_func(self):
        return self.get_object() == self.request.user


class UserTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.request.user
        return context




from django.contrib.auth.models import User
from django.views.generic import CreateView

from users.forms import RegistrationForm


class RegistrationView(CreateView):
    model = User
    # fields = ('username', 'email', 'first_name', 'last_name', 'password')
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'users/user_form.html'


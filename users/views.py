from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CreateUserForm


class CreateUserView(CreateView):
    model = User
    template_name = 'create_user.html'
    success_url = reverse_lazy('login')
    form_class = CreateUserForm


class LoginUserView(LoginView):
    model = User
    template_name = 'login.html'
    next_page = reverse_lazy('index')


class LogoutUserView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')

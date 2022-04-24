from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView

from . forms import cUserCreationForm


class SignUpView(CreateView):
    form_class = cUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/signup.html' 


class cLoginView(LoginView):
    template_name = 'authentication/login.html'

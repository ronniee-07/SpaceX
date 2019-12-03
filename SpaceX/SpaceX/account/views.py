from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView,TemplateView
# Create your views here.

class Signup(CreateView):
    form_class = forms.UserSignupForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

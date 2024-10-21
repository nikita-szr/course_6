from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib.auth.views import LoginView

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        form.send_welcome_email()

        login(self.request, user)

        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
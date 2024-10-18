from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def send_welcome_email(self):
        email = self.cleaned_data['email']
        send_mail(
            'Здавствуйте!',
            'Спасибо за регистрацию!',
            'test@example.com',
            [email],
            fail_silently=False,
        )
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	email = forms.EmailField()
	is_staff = forms.BooleanField()
	avatar = forms.ImageField()

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'is_staff', 'avatar',)
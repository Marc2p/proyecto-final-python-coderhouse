from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	email = forms.EmailField()
	avatar = forms.ImageField()

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'avatar',)

class EditProfileForm(UserChangeForm):
	password = None
	avatar = forms.ImageField(required=False)

	class Meta:
		model = User
		fields = ('username', 'email', 'avatar',)

class 	changePermissionsForm(forms.ModelForm):
	pass
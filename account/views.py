from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from account.forms import SignUpForm
from account.models import Avatar

# Create your views here.

def signup_view(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		ctx = {
			'form': SignUpForm(),
			'titulo': 'Registro de usuario',
			'enviar': 'Registrarse',
		}
		return render(request, 'account.html', ctx)

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('index')
	else:
		ctx = {
			'form': AuthenticationForm(),
			'titulo': 'Iniciar sesión',
			'enviar': 'Iniciar sesión',
		}
		return render(request, 'account.html', ctx)
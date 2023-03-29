from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from account.forms import SignUpForm, EditProfileForm
from account.models import Avatar
from django.contrib.auth.decorators import login_required

# Create your views here.

def is_staff(user):
	return user.is_staff

def signup_view(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			avatar = Avatar(user=user, avatar=request.FILES['avatar'])
			avatar.save()
			login(request, user)
			return redirect('index')
		else:
			ctx = {
				'form': form,
				'titulo': 'Registro de usuario',
				'enviar': 'Registrarse',
			}
			return render(request, 'account.html', ctx)
	else:
		ctx = {
			'form': SignUpForm(),
			'titulo': 'Registro de usuario',
			'enviar': 'Registrarse',
		}
		return render(request, 'account.html', ctx)

def login_view(request):
	if request.user.is_authenticated:
		return redirect('index')
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
				'form': form,
				'titulo': 'Iniciar sesión',
				'enviar': 'Iniciar sesión',
			}
			return render(request, 'account.html', ctx)
	else:
		ctx = {
			'form': AuthenticationForm(),
			'titulo': 'Iniciar sesión',
			'enviar': 'Iniciar sesión',
		}
		return render(request, 'account.html', ctx)

@login_required
def editar_perfil(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, request.FILES, instance=request.user)
		if form.is_valid():
			user = form.save()
			if 'avatar' in request.FILES:
				avatar = Avatar(user=user, avatar=request.FILES['avatar'])
				avatar.save()
			return redirect('index')
		else:
			ctx = {
				'form': form,
				'titulo': 'Editar perfil',
				'enviar': 'Guardar',
			}
			return render(request, 'account.html', ctx)
	else:
		ctx = {
			'form': EditProfileForm(instance=request.user),
			'titulo': 'Editar perfil',
			'enviar': 'Guardar',
		}
		return render(request, 'account.html', ctx)

@login_required
def cambiar_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('index')
		else:
			ctx = {
				'form': form,
				'titulo': 'Cambiar contraseña',
				'enviar': 'Guardar',
			}
			return render(request, 'account.html', ctx)
	else:
		ctx = {
			'form': PasswordChangeForm(request.user),
			'titulo': 'Cambiar contraseña',
			'enviar': 'Guardar',
		}
		return render(request, 'account.html', ctx)


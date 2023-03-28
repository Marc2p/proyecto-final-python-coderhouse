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

# crear una vista para modificar un usuario, que solo pueda modificar su propio usuario. Si el método es POST, se debe validar el formulario y si es válido, se debe guardar el usuario y redirigir a la página de inicio. Si el método es GET, se debe mostrar el formulario con los datos del usuario.
def update_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST, request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		ctx = {
			'form': SignUpForm(instance=request.user),
			'titulo': 'Actualizar usuario',
			'enviar': 'Actualizar',
		}
		return render(request, 'account.html', ctx)
from django.contrib import admin
from django.urls import path, include
from account.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
		path('signup/', signup_view, name='signup'),
		path('login/', login_view, name='login'),
		path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
		path('edituser', editar_perfil, name='edituser'),
		path('changepass', cambiar_password, name='changepass'),
]
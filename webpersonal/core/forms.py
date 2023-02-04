from django import forms
from django.forms import ModelForm
from.models import Noticia, Comentarios, Perfil, User, Autor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Modelos de formularios

class Nuevanoticia(ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'slug', 'portada', 'pie_portada', 'cuerpo', 'seccion']


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class Editar_userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

class Profilepicform(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['profilepic']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre_autor','descripcion', 'twitter', 'gmail', 'ig']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['comentario']
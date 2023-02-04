from django.shortcuts import render, redirect
from .models import Noticia,Perfil, Comentarios, Autor
from .forms import Nuevanoticia, CustomUserForm, CommentForm, Editar_userForm, Profilepicform, AutorForm
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from django.views.generic import UpdateView
from django.urls import reverse_lazy
import os
# Create your views here.

html_base = """
    
"""

#-----------------------------------------------------------------------------------------------#
                                            #Vistas de post

def home(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.all().order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda)
        ).order_by('-creacion').distinct()
        return render(request,'core/busqueda.html',{"noticias": noticias})
    portada = Noticia.objects.filter(es_portada = True).order_by('-creacion')[:1]
    return render(request,'core/home.html',{"noticias": noticias, "portada":portada})

def actualidad(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 1).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 1)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/actualidad.html',{"noticias": noticias})

def cronica(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 2).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 2)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/cronica.html',{"noticias": noticias})

def internacionales(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 3).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 3)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/internacionales.html',{"noticias": noticias})

def deportes(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 4).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 4)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/deportes.html',{"noticias": noticias})

def insolito(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 5).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 5)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/insolito.html',{"noticias": noticias})

def tendencias(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 6).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 6)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/tendencias.html',{"noticias": noticias})

def farandula(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 7).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 7)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/farandula.html',{"noticias": noticias})

def tecnologia(request):
    busqueda = request.GET.get("buscar")
    noticias = Noticia.objects.filter(seccion = 8).order_by('-creacion')
    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda, seccion = 8)
            
        ).order_by('-creacion').distinct()
    return render(request,'secciones/tecnologia.html',{"noticias": noticias})

def detalle_noticia(request,slug):
    noticias = Noticia.objects.get(
        slug = slug
    )
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if request.user.is_anonymous:
            return redirect('login')
        else:
            if form.is_valid():
                comment = form.save(commit = False)
                comment.autor = request.user.perfil
                comment.noticia = noticias
                comment.save()
                form = CommentForm()
            else:
                print(form.errors)
    similares = Noticia.objects.filter(seccion = noticias.seccion).exclude(titulo = noticias.titulo).order_by('-creacion')[:3]
    recomendados = Noticia.objects.exclude(seccion = noticias.seccion).order_by('-creacion')[:6]
    comentarios = Comentarios.objects.filter(noticia=noticias).order_by('-creacion')

    return render(request,'core/publicacion.html',{"noticias": noticias, "similares": similares, "recomendados": recomendados , "comentarios": comentarios, "form":form})

def actualizar_comentario(request, id):
    comentario = Comentarios.objects.get(id = id)
    form=CommentForm(instance=comentario)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comentario)
        if form.is_valid() and comentario.autor == request.user.perfil:
            form.save()
        else:
           print(form.errors)
    return render(request,'core/modificar_comentario.html',{"comentario":comentario, "form":form})

def eliminar_comentario(request, id):
    comentario = Comentarios.objects.get(id=id)
    comentario.delete()
    return redirect(to = "home")
#-----------------------------------------------------------------------------------------------#
                                            #Vistas Info
def about(request):
    return render(request,'core/about.html')

def contact(request):
    return render(request,'core/contact.html')

#-----------------------------------------------------------------------------------------------#
                    #Vistas de ingreso, modificación y eliminación de post

@permission_required('core.view_noticia')
def listado_noticias(request):
    if request.user.perfil.es_editor or request.user.is_staff:
        noticias = Noticia.objects.all().order_by('-creacion')
        data = {
            'Noticias':noticias
        }        
    else:
        noticias = Noticia.objects.filter(autor = request.user.perfil.autor).order_by('-creacion')
        data = {
            'Noticias':noticias
        }     
    return render(request,'core/listado_noticias.html',data)

@permission_required('core.add_noticia')
def nueva_noticia(request):
    data = {
        'form':Nuevanoticia()
    }
    if request.method == 'POST':
        formulario = Nuevanoticia(request.POST, request.FILES)
        if formulario.is_valid():
            noticia = formulario.save(commit=False)
            noticia.autor = request.user.perfil.autor
            noticia.save()
            data['mensaje'] = 'Publicado correctamente'
        else:
            print(formulario.errors)

    return render(request,'core/nueva_noticia.html', data)
    
@permission_required('core.change_noticia')
def modificar_noticia(request, id):
    if request.user.is_staff:
        noticia = Noticia.objects.get(id=id)
    else:
        noticia = Noticia.objects.get(id=id, autor = request.user.perfil.autor.id)
    data = {
        'form':Nuevanoticia(instance=noticia)
    }
    if request.method == 'POST':
        formulario = Nuevanoticia(data = request.POST, instance=noticia)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Modificado correctamente'
            data['form'] = formulario
        else:
            data['mensaje'] = 'No ha funcionado'
            print(formulario.errors)
    return render(request,'core/modificar_noticia.html',data)

@permission_required('core.delete_noticia')
def eliminar_noticia(request, id):
    noticia = Noticia.objects.get(id=id)
    noticia.delete()
    return redirect(to="lista")

#-----------------------------------------------------------------------------------------------#
                            #Vistas de login, logout, register

def log_in(request):         
    return render(request,'registration/login.html')
    
def Log_out(request):
    logout(request)
    return redirect('home')

def registro(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            group = Group.objects.get(name='Lector')
            user.groups.add(group)
            login(request,user)
            return redirect(to='home')
        else:
            data['mensaje'] = 'No ha funcionado'
    return render(request,'registration/registro.html', data)

#-----------------------------------------------------------------------------------------------#
                            #Vistas de perfil

def perfil(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
            perfil = User.objects.get(username = username)
            if perfil.perfil.es_lector:
                #No hay nada que mostrar en user
                pass
            else:
                #Obtiene las publicaciones del autor
                post = Noticia.objects.filter(autor = perfil.perfil.autor.id)
    else:
        perfil = current_user
        if perfil.perfil.es_lector:
            #No hay nada que mostrar
            pass
            return render(request,'core/perfil.html', {"perfil":perfil})
        else:
            #Obtiene las publicaciones del user activo
            post = Noticia.objects.filter(autor = current_user.perfil.autor.id)
        
    return render(request,'core/perfil.html', {"perfil":perfil , "post": post})

class editar_foto_perfil(UpdateView):
    model = perfil
    template_name = 'core/modificar_user.html'
    form_class = Profilepicform
    success_url = reverse_lazy('home')

def editar_profilepic(request,username=None):
    current_user = request.user
    perfil = Perfil.objects.get(usuario = current_user.id)
    form = Profilepicform(instance=request.user.perfil)
    if username and username != current_user.username:
        pass
    else:
        if request.method == "POST":
            form = Profilepicform(request.FILES , instance = perfil)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)
    return render(request, 'core/modificar_user.html',{"form": form})

def editar_user(request,username=None):
    current_user = request.user
    user = User.objects.get(username = current_user)
    form = Editar_userForm(instance=user)
    if username and username != current_user.username:
        pass
    else:
        if request.method == "POST":
            form = Editar_userForm(request.POST, instance = user)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)
    return render(request, 'core/modificar_user.html',{"form": form})

def editar_autor(request,username):
    username = request.user.username
    autor = Autor.objects.get(user_id = request.user.perfil.id)
    form = AutorForm(instance=autor)
    if request.user.perfil.autor != autor:
        pass
    else:
        if request.method == "POST":
            form = AutorForm(request.POST, instance = autor)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)
    return render(request, 'core/modificar_user.html',{"form": form})
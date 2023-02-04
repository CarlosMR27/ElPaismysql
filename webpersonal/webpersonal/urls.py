"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from core import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.home, name='home'),
    path('actualidad/', views.actualidad, name='actualidad'),
    path('cronica/', views.cronica, name='cronica'),
    path('internacionales/', views.internacionales, name='internacionales'),
    path('deportes/', views.deportes, name='deportes'),
    path('insolito/', views.insolito, name='insolito'),
    path('tendencias/', views.tendencias, name='tendencias'),
    path('farandula/', views.farandula, name='farandula'),
    path('tecnlogia/', views.tecnologia, name='tecnologia'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('listado_noticias/', views.listado_noticias, name='lista'),
    path('nueva_noticia/', views.nueva_noticia, name='agregar'),
    path('modificar_noticia/<id>/', views.modificar_noticia, name='modificar'),
    path('eliminar_noticia/<id>/', views.eliminar_noticia, name='eliminar'),
    path('admin/', admin.site.urls , name='admin'),
    path('login/', views.login, name='login'),
    path('',views.logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.registro, name='registro'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('<slug:slug>', views.detalle_noticia, name='publicacion'),
    path('perfil/<str:username>', views.perfil, name='perfil'),
    path('modificar_user/<str:username>', views.editar_user, name='editar_user'),
    path('modificar_autor/<str:username>', views.editar_autor, name='editar_autor'),
    path('modificar_comentario/<id>/', views.actualizar_comentario, name='actualizar_comentario'),
    path('eliminar_comentario/<id>/', views.eliminar_comentario, name='eliminar_coment'),
    path('editar_foto_perfil/<str:username>', views.editar_profilepic, name='editar_perfil'),
    #path('editar_foto_perfil/<pk>', views.editar_foto_perfil.as_view(), name='editar_perfil'),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

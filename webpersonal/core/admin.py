from django.contrib import admin
from .models import Noticia, Seccion, Perfil, Autor, Comentarios

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'seccion', 'autor','creacion','update']
    search_fields = ['titulo', 'seccion']
    list_filter = ['seccion','creacion','autor']
    list_per_page = 15

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario']
    search_fields = ['usuario']
    list_filter = ['es_autor','es_lector','es_editor']
    list_per_page = 15

class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre_autor']
    search_fields = ['nombre_autor']
    list_per_page = 15

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['autor','noticia','creacion','update']
    search_fields = ['autor']
    list_filter = ['creacion','update']
    list_per_page = 15


# Register your models here.
admin.site.register(Seccion)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Comentarios,ComentarioAdmin)


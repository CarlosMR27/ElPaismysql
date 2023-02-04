from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Seccion(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'
    
    def __str__(self):
        return self.name

class Perfil(models.Model):
    
    #Guarda las fotos a usuarios/nombre del usuario/fotos/nombre de la foto 
    def user_directory_path(instance, filename):
         return 'Usuarios/{0}/Fotos/{1}'.format(instance.usuario.username, filename)

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    profilepic = models.ImageField(default = 'inicio_edit.png',upload_to=user_directory_path)
    es_editor = models.BooleanField(default=False)
    es_autor = models.BooleanField(default=False)
    es_lector = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return "{0} {1}".format(self.usuario.first_name, self.usuario.last_name)

class Autor(models.Model):
    nombre_autor = models.CharField(max_length=(50),blank=False, null= False)
    descripcion = RichTextField()
    twitter = models.CharField(max_length=(400),blank=True, null= True)
    ig = models.CharField(max_length=(400),blank=True, null= True)
    gmail = models.CharField(max_length=(400),blank=True, null= True)
    user = models.OneToOneField(Perfil, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombre_autor
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=(300), blank=False, null= False)
    slug = models.CharField(max_length=(50), blank=False, null= False)
    portada = models.ImageField(upload_to='noticia/%Y/%m/%d')
    pie_portada = models.CharField(max_length=(100), blank=True, null= True)
    cuerpo = RichTextField()
    creacion = models.DateTimeField(auto_now_add=True)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    update = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    es_portada = models.BooleanField(default=False)
    es_visible = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return "{0} {1}".format(self.titulo, self.autor)

class Comentarios(models.Model):
    autor = models.ForeignKey(Perfil, on_delete= models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, null=True)
    comentario = models.TextField()
    es_visible = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return self.autor.usuario.username
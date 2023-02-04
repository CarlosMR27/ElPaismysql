from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Perfil, Autor
from django.contrib.auth.models import Group
from django.dispatch import receiver

#Para crear un perfil automáticamente
@receiver(post_save, sender = User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
       Perfil.objects.create(usuario=instance)

#Para cambiar el grupo y las variables de Perfil del autor
@receiver(post_save, sender = Autor)
def cambiar_permisos(sender, instance, created, **kwargs):
    if created:
        autor = Perfil.objects.get(autor=instance)
        autor.es_lector = False
        autor.es_autor = True
        autor.save()
        group1 = Group.objects.get(name='Lector')
        group2 = Group.objects.get(name='Autor')
        instance.user.usuario.groups.remove(group1)
        instance.user.usuario.groups.add(group2)
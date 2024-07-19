from django.contrib import admin
from .models import Coffe, Publication, Comment, Contacts, ClientContact
# Register your models here.

@admin.register(Coffe)
class CoffeAdmin(admin.ModelAdmin):
    list_display = ['name' ]


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Comment)
class PublicationComment(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Contacts)
class PublicationContacts(admin.ModelAdmin):
    list_display = ['email']

@admin.register(ClientContact)
class PublicationClient(admin.ModelAdmin):
    list_display = ['name',]

   #
   # def has_add_permission(self, request):
   #      return False
   #
   #  def has_change_permission(self, request, obj=None):
   #      return False
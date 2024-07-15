from django.contrib import admin
from .models import Coffe, Publication, Comment, Contacts
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
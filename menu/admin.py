from django.contrib import admin
from .models import Coffe, Publication
# Register your models here.

@admin.register(Coffe)
class CoffeAdmin(admin.ModelAdmin):
    list_display = ['name' ]


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title']
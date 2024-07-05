from django.contrib import admin
from .models import Coffe
# Register your models here.

@admin.register(Coffe)
class CoffeAdmin(admin.ModelAdmin):
    list_display = ['name' ]

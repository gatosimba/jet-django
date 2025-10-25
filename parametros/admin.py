from django.contrib import admin
from .models import Parametro


@admin.register(Parametro)
class ParametroAdmin(admin.ModelAdmin):
    list_display = ("nome", "valor", "descricao")
    search_fields = ("nome",)

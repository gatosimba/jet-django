from django.contrib import admin
from .models import Empresa, Filial, Funcionario


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cnpj", "email", "telefone")
    search_fields = ("nome", "cnpj")


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_display = ("nome", "empresa", "cidade", "estado", "ativa")
    list_filter = ("empresa", "ativa")
    search_fields = ("nome", "cnpj", "cidade")


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "cargo", "empresa", "filial", "ativo")
    list_filter = ("empresa", "filial", "ativo")
    search_fields = ("nome", "cpf", "cargo")

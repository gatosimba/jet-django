from django.db import models
from django.utils import timezone

#from validate_docbr import CPF, CNPJ
from .validators import *


class Empresa(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    cnpj = models.CharField(max_length=18, validators=[validate_cnpj], unique=True)
    razao_social = models.CharField(max_length=200)
    inscricao_estadual = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Filial(models.Model):
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name="filiais"
    )
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18, validators=[validate_cnpj], unique=True)
    endereco = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    ativa = models.BooleanField(default=True)
    data_abertura = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Filial"
        verbose_name_plural = "Filiais"
        unique_together = ("empresa", "nome")
        ordering = ["empresa", "nome"]

    def __str__(self):
        return f"{self.nome} ({self.empresa.nome})"


class Funcionario(models.Model):
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name="funcionarios"
    )
    filial = models.ForeignKey(
        Filial,
        on_delete=models.PROTECT,
        related_name="funcionarios"
    )
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, validators=[validate_cpf], unique=True)
    cargo = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    data_admissao = models.DateField(default=timezone.now)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.cargo} - ({self.filial.nome})"

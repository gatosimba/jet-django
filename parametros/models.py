from django.db import models

class Parametro(models.Model):
    """
    Modelo para armazenar parâmetros do sistema com nome, valor e descrição.
    """
    nome = models.CharField(
        max_length=100,
        help_text="Nome único para identificar o parâmetro.",
        unique=True,
        verbose_name="Nome"
    )
    valor = models.CharField(
        max_length=128,
        help_text="Valor do parâmetro. Pode ser texto, número, etc.",
        blank=True, # Permite que o valor seja deixado em branco se necessário
        verbose_name="Valor"
    )
    descricao = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        help_text="Descrição detalhada do parâmetro.",
        verbose_name="Descrição"
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de Criação"
    )
    data_modificacao = models.DateTimeField(
        auto_now=True,
        verbose_name="Data de Modificação"
    )

    def __str__(self):
        return f"{self.nome} - {self.valor} - {self.descricao}"

    class Meta:
        verbose_name = "Parâmetro"
        verbose_name_plural = "Parâmetros"
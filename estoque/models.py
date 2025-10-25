from django.db import models

from django.utils.translation import gettext_lazy as _

class Produto(models.Model):
    """
    Modelo para armazenar Produtos do sistema.
    """
    nome = models.CharField(
        max_length=100,
        help_text=_("Nome único para identificar o Produto."),
        unique=True,
        verbose_name=_("Nome do Produto")
    )
    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
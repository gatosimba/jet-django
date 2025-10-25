# your_app/validators.py
from django.core.exceptions import ValidationError
from validate_docbr import CPF, CNPJ

def validate_cpf(value):
    cpf = CPF()
    if not cpf.validate(value):
        raise ValidationError("Número de CPF inválido.", code="invalid_cpf")

def validate_cnpj(value):
    cnpj = CNPJ()
    if not cnpj.validate(value):
        raise ValidationError("Número de CNPJ inválido.", code="invalid_cnpj")

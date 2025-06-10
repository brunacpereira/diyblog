from django import template
from django.template.loader import get_template
from django.core.paginator import Paginator

register = template.Library()


@register.filter(name="indice")
def indice(value, arg):

    numero_inteiro = int(value)

    return value
from django import template
from django.utils.safestring import mark_safe
from .base import get_script, get_styles

register = template.Library()


@register.simple_tag
def bootstrap_script(use_min=True):
    return mark_safe(f'<script type="text/javascript" src="{get_script(use_min)}"></script>')


@register.simple_tag
def bootstrap4_style(theme='default', use_min=True):
    return mark_safe(f'<link rel="stylesheet" href="{get_styles(4, theme, use_min)}" type="text/css">')


@register.simple_tag
def bootstrap3_style(theme='default', use_min=True):
    return mark_safe(f'<link rel="stylesheet" href="{get_styles(3, theme, use_min)}" type="text/css">')

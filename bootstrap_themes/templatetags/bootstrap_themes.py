from django import template
from django.utils.safestring import mark_safe
from .. import get_styles

register = template.Library()


@register.simple_tag
def bootstrap_styles(theme='default'):
    mimetype = 'text/css'
    return mark_safe('<link rel="stylesheet" href="%(theme)s" type="%(mimetype)s">'
                     % dict(theme=get_styles(theme), mimetype=mimetype))

from django import template
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.safestring import mark_safe
from .. import get_script, get_styles

register = template.Library()


@register.simple_tag
def bootstrap_script(use_min=True):
    return mark_safe(
        '<script type="text/javascript" src="%(script_file)s"></script>' % dict(script_file=get_script(use_min)))


@register.simple_tag
def bootstrap_styles(theme='default', type='min.css'):
    mimetype = 'text/css'
    return mark_safe('<link rel="stylesheet" href="%(theme)s" type="%(mimetype)s">'
                     % dict(theme=get_styles(theme), mimetype=mimetype))

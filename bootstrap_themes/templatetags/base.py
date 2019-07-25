from django.contrib.staticfiles.storage import staticfiles_storage
from ..themes import bootstrap4_themes, bootstrap3_themes


def get_script(version=4, use_min=True):
    minified = '.min' if use_min else ''
    if version not in [3, 4]:
        raise KeyError("Bad version [{version}], available 3 & 4")
    return staticfiles_storage.url(f'bootstrap/themes/{version}/default/bootstrap{minified}.js')


def get_styles(version=4, theme='default', use_min=True):
    selected_theme = 'default'
    minified = '.min' if use_min else ''
    if version not in [3, 4]:
        raise KeyError("Bad version [{version}], available 3 & 4")
    available_themes = bootstrap4_themes if version == 4 else bootstrap3_themes
    if (any(theme in t for t in available_themes)):
        selected_theme = theme
    else:
        raise KeyError(f"Theme not available [{theme}] using default")
    return staticfiles_storage.url(f"bootstrap/themes/{version}/{selected_theme}/bootstrap{minified}.css")

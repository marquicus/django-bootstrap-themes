from django.utils.text import slugify
import requests


api_bootstrap = {
    'bt3': 'http://bootswatch.com/api/3.json',
    'bt4': 'http://bootswatch.com/api/4.json'
}
available_themes = {
    'default_bt3': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
    'default_bt4': 'https://maxcdn.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css',
}
for key, url in api_bootstrap.items():
    theme_api = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0 (compatible)'})
    for _, theme in enumerate(theme_api.json()["themes"]):
        available_themes[slugify(theme["name"] + "_" + key)] = theme["cssCdn"]


def list_themes():
    return available_themes.items()

def get_script(use_min=True):
    minified = '.min' if use_min else ''

    return staticfiles_storage.url('bootstrap/js/bootstrap%(minified)s.js' % dict(minified=minified))

def get_styles(theme='default', use_min=True):
    selected_theme='default'
    minified = '.min' if use_min else ''
    try:
        if theme in available_themes:
            selected_theme=theme
    except KeyError:
        print("Theme not available [%s] using default" % theme)
    return staticfiles_storage.url('bootstrap/themes/%(theme)s/css/bootstrap%(minified)s.css' % dict(theme=theme))

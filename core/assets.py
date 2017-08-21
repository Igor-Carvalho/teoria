"""Gerenciamento de assets."""

import django_assets

js_files = [
    'js/*.js'
]
js = django_assets.Bundle(*js_files, filters='uglifyjs', output='js/bundle.min.js')

css_files = [
    'css/poole.css',
    'css/hyde.css',
    'css/theme.css',
    'css/base.css',
]
css = django_assets.Bundle(*css_files, filters='cssmin', output='css/bundle.min.css')

django_assets.register('js_all', js)
django_assets.register('css_all', css)

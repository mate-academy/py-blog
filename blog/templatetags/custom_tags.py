from datetime import datetime

from django import template

register = template.Library()


@register.simple_tag
def url_reparse(request, **kwargs):
    params = request.GET.copy()

    for k, v in kwargs.items():
        if v:
            params[k] = v
        else:
            params.pop(k)

    result = request.path

    if len(params):
        result += '?' + params.urlencode()

    return result

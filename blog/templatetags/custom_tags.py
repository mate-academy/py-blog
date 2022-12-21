from django import template

register = template.Library()


@register.simple_tag
def url_reparse(request, **kwargs):
    params = request.GET.copy()

    for key, value in kwargs.items():
        if value:
            params[key] = value
        else:
            params.pop(key)

    result = request.path

    if len(params):
        result += "?" + params.urlencode()

    return result

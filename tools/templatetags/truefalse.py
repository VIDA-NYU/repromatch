from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
def truefalse(value): # Boolean
    """Converts a bollean into an icon"""
    base = '<img style="height:0.8em;" src="/static/images/%s.png" alt="%s"/>'
    if value == "true" or value is True:
        return mark_safe( base % ('check-64', True))
    return mark_safe( base % ('delete_2', False))


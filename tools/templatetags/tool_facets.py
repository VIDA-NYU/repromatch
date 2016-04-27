from django import template
from django.utils.safestring import mark_safe

from  urlparse import urlsplit, urlunsplit

from tools.models import Tool

import re

register = template.Library()

@register.filter(is_safe=True)
def facet_breadcrumb(url):
    """Extracts current facets from url and returns breadcrumb links
       Currently assumes each facet is in its own selected_facets query
    """
    header = '<br/><b>Current filter (click to remove):</b>'
    
    parsed_url = list(urlsplit(url))
    query = parsed_url[3]
    facets = query.split('&')
    breadcrumb = []
    for i, facet in enumerate(facets):
        if facet.startswith('selected_facets='):
            values = facet.split('=')[1].split(':')
            other_facets = facets[:i] + facets[i+1:]
            query = '&'.join(other_facets)
            url_copy = [p for p in parsed_url]
            url_copy[3] = query
            new_url = urlunsplit(url_copy)
            name = values[0][:-6]
            value = values[1]
            desc_map = {'NONE':'None','LOW':'Low','MEDIUM':'Medium','HIGH':'High','false':'No','true':'Yes'}
            value = desc_map.get(value, value)
            verbose_name = Tool._meta.get_field_by_name(name)[0].verbose_name
            a = '<br/><a class="subsection" href="%s">%s</a>' % (new_url, '%s: %s' % (verbose_name, value))
            breadcrumb.append(a)
    if breadcrumb:
        breadcrumb.insert(0, header)
    return mark_safe(' '.join(breadcrumb))



@register.filter(is_safe=True)
def as_table(url):
    url = re.sub("&page=(\d*)", '', url)
    return mark_safe(url.replace('tools/search', 'tools/search_table'))

@register.filter(is_safe=True)
def as_list(url):
    url = re.sub("&page=(\d*)", '', url)
    return mark_safe(url.replace('tools/search_table', 'tools/search'))

@register.filter(is_safe=True)
def no_page(url):
    """ Remove &page=* from url """
    url = re.sub("&page=(\d*)", '', url)
    return mark_safe(url)


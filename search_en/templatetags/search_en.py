# search.templatetags.class_name.py
from django import template

register = template.Library()


@register.filter()
def fu_search_en(value):
    return value.__class__.__name__

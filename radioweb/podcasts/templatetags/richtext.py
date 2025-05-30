from django import template
from wagtail.rich_text import RichText

register = template.Library()

@register.filter
def richtext(value):
    if isinstance(value, RichText):
        return value.source
    return value

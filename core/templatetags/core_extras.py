from django import template

register = template.Library()

@register.filter
def replace(value, args):
    """Remplace les occurrences de old dans value par new."""
    old, new = args.split(',', 1)
    return value.replace(old, new)
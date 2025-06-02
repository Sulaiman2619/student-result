# thai_date.py
from django import template

register = template.Library()

@register.filter
def buddhist_date(value, fmt="%d/%m/%Y"):
    try:
        value = value.replace(year=value.year + 543)
        return value.strftime(fmt)
    except Exception:
        return "-"

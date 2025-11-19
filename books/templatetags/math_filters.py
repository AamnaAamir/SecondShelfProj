# from django import template

# register = template.Library()

# @register.filter
# def mul(value, arg):
#     """
#     Multiply two numeric values.
#     Usage: {{ price|mul:quantity }}
#     """
#     try:
#         return float(value) * float(arg)
#     except Exception:
#         return ''

#or
# books/templatetags/math_filters.py
from django import template
register = template.Library()

@register.filter
def mul(value, arg):
    try:
        return int(value) * int(arg)
    except Exception:
        return ''

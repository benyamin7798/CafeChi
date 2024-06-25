# shopping_cart/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        return 0

@register.filter
def total_price(order_items):
    total = sum(item.quantity * item.product.price for item in order_items)
    return total

from django import template

register = template.Library()

@register.filter
def multiply(value1, value2):
    return value1 * value2

@register.filter
def sum_total(cart_items):
    total = sum(item.quantity * item.product_id.price for item in cart_items)
    return total


@register.filter
def sum_quantity(cart_items):
    """Return the total quantity of products in the cart."""
    return sum(item.quantity for item in cart_items)

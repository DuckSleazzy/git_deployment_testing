from django import template

register = template.Library()

@register.filter(name="le_testing") # this is the decorator way
def le_slaughtering(value,arg):
    # cuts out all values of part from string
    return value.replace(arg,"")

# register.filter("le_testing",le_slaughtering) this is one way to do it
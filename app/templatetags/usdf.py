from django import template
register=template.Library()
@register.filter()
def swap(value):
    return value.swapcase()
#register.filter('swapping',swap)

def counting(value,arg):
    return value.count(arg)
register.filter('counting',counting)


def remove(value,arg):
    return value.replace(arg,'')
register.filter('remove',remove)
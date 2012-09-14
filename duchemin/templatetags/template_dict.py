from django.template.defaultfilters import register


@register.filter(name='lookup')
def lookup(d, index):
    return d.get(index, '')

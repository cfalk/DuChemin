from django.template.defaultfilters import register


@register.filter(name='expandvoice')
def expandvoice(voice):
    if voice.lower() == "t":
        return "Tenor"
    elif voice.lower() == "ct":
        return "Contratenor"
    elif voice.lower() == "s":
        return "Superius"
    elif voice.lower() == "b":
        return "Bassus"
    else:
        return voice

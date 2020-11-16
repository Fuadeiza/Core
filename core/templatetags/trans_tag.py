from django import template
from django.utils.translation import ugettext

register = template.Library()


@register.filter(name='template_trans')
def template_trans(text):
    # try:
    return ugettext(text)
    # except:
    #     return text
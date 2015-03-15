from django import template
from django.core.urlresolvers import reverse
from django.utils.encoding import iri_to_uri

register = template.Library()


@register.inclusion_tag('templatetags/link_tag.html', takes_context=True)
def nav_link(context, text, url_pattern=None, css_class=None, *args, **kwargs):
    """
    Renders a link (<a>) tag with provided text and pointing to url resolved using
    url pattern name and url args and kwargs provided. Optional css-class string sets
    the value for link tag's 'class' attribute.

    Regardless of 'css_class' argument being provided or not, resulting tag is rendered with
    'class' attribute set to (or extended with) 'active' postfix depending on whether the
    current request path starts with the link's 'href' value. If the the link is supposed to point
    to the site root, the comparison is strict - 'active' class is added only if we're in the site root.

    Example usages:

    {% nav_link _("User Details") 'user_detail' pk=1 %}
    {% nav_link _("Tickets") 'tech_tickets' css_class='additional css class string' %}
    {% nav_link _("another user details") 'user_detail' pk=2 css_class='specific css class' %}

    :param text: link text
    :param url_pattern: ulr pattern name to resolve the link tag to
    :param css_class: additional css classes string to be applied to link tag 'class' attribute
    :param args: ulr pattern args
    :param kwargs: ulr pattern kwargs
    """
    if url_pattern:
        url = reverse(url_pattern, args=args, kwargs=kwargs)
    else:
        url = '#'

    request_path = context['request'].path

    if url == '/':
        active = url == request_path
    else:
        uri = iri_to_uri(request_path)
        active = uri.startswith(url)

    return {
        'url': url,
        'text': text,
        'css_class': css_class,
        'active': active
    }


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
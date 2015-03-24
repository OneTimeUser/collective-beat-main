class ForceDefaultLanguageMiddleware(object):
    """
    Ignore Accept-Language HTTP headers
    
    This will force the I18N machinery to always choose settings.LANGUAGE_CODE
    as the default initial language, unless another one is set via sessions or cookies
    
    Should be installed *before* any middleware that checks request.META['HTTP_ACCEPT_LANGUAGE'],
    namely django.middleware.locale.LocaleMiddleware

    https://docs.djangoproject.com/en/1.7/topics/i18n/translation/#how-django-discovers-language-preference
    https://djangosnippets.org/snippets/218/
    https://djangosnippets.org/snippets/10469/
    """

    def process_request(self, request):
        # request.META['HTTP_ACCEPT_LANGUAGE'] = ''
        del request.META['HTTP_ACCEPT_LANGUAGE']

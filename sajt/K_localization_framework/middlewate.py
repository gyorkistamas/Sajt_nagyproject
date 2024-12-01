from django.utils.translation import activate

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang_code = request.session.get('lang_code', 'en')
        activate(lang_code)
        respo = self.get_response(request)
        return respo
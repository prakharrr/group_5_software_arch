from time import sleep
from django.utils.deprecation import MiddlewareMixin

class SessionMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        print(get_response)
        print("happens?")

    def __call__(self, request):
        print("call")
        self.check_session_expiry(request)
        return self.get_response(request)

    def check_session_expiry(self, request):
        print("hit")
        print(request.session.get_expiry_age())

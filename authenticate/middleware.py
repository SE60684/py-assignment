from django.http import HttpResponse
from django.conf import settings
from utils import header_utils
import jwt




def require_authenticate(request):
    path = request.path
    for item in settings.JWT_NOT_REQUIRE_AUTHENTICATE:
        if path.startswith(item):
            return False
    return True


def validate_token(token):
    try:
        jwt.decode(token, settings.JWT_SECRET_KEY)
        return True
    except jwt.exceptions.DecodeError:
        return False


def simple_middleware(get_response):
    # One-time configuration and initialization.
    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if require_authenticate(request):
            header = header_utils.get_header(request)
            token = header['HTTP_TOKEN']

            if not validate_token(token):
                response = HttpResponse()
                response.status_code = 401
                response.content = 'Access denied'
                return response

        response = get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
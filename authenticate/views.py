from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from utils import header_utils
from django.conf import settings
import jwt

username_header = 'HTTP_USERNAME'

@csrf_exempt
def get_token(request):
    header = header_utils.get_header(request)
    username = header[username_header]
    token = jwt.encode({'username': username}, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return HttpResponse(token)



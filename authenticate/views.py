from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from utils import header_utils
from authenticate.models import User
from mongoengine import connect
from django.conf import settings
import jwt

username_header = 'HTTP_USERNAME'
password_header = 'HTTP_PASSWORD'

@csrf_exempt
def login(request):
    header = header_utils.get_header(request)
    username = header[username_header]
    password = header[password_header]

    connect(settings.MONGOBD_ALIAS)
    user = User.objects(username=username, password=password).first()
    if user is not None:
        token = jwt.encode({'username': username}, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return HttpResponse(token)
    else:
        return HttpResponse('Login failed')


@csrf_exempt
def register(request):
    header = header_utils.get_header(request)
    username = header[username_header]
    password = header[password_header]

    connect(settings.MONGOBD_ALIAS)
    user = User.objects(username=username).first()
    if user is not None:
        return HttpResponse('Username is exist!')
    user = User()
    user.username = username
    user.password = password
    user.save()

    return HttpResponse('Register successful')



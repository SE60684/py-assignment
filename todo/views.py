from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from todo.models import *
from utils import json_utils
import json
# Create your views here.


@csrf_exempt
def index(request, id):
    connect('test')
    if request.method == 'GET':
        post = Post.objects(uid=id).first()
        if post is None:
            return HttpResponse("Instance is not exist")
        else:
            return HttpResponse(json_utils.mongo_to_json(post), content_type="application/json")

    elif request.method == 'POST' or request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        post = Post.objects(uid=id).first()
        if post is None:
            post = Post()
            post.uid = id

        for key in data:
            setattr(post, key, data[key])
        post.save()
        return HttpResponse(json_utils.mongo_to_json(post), content_type="application/json")

    elif request.method == 'DELETE':
        post = Post.objects(uid=id).first()
        if post is None:
            return HttpResponse("Instance is not exist")
        else:
            post.delete()
            return HttpResponse("Delete successful")
    else:
        return HttpResponse("Method not support:" + request.method)



@csrf_exempt
def list(request):
    connect('test')
    if request.method == 'GET':
        posts = Post.objects().order_by("index")
        return HttpResponse(json_utils.mongo_to_json(posts), content_type="application/json")

    elif request.method == 'POST' or request.method == 'PUT':
        datas = json.loads(request.body.decode('utf-8'))
        for data in datas:
            id = data["uid"]
            post = Post.objects(uid=id).first()
            if post is None:
                post = Post()
                post.uid = id

            for key in data:
                setattr(post, key, data[key])
            post.save()
        return HttpResponse("Update all successful")

    elif request.method == 'DELETE':
        Post.objects().delete()
        return HttpResponse("Delete all successful")
    else:
        return HttpResponse("Method not support:" + request.method)



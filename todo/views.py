from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from todo.models import *
from utils import json_utils
from django.conf import settings
import json
# Create your views here.


@csrf_exempt
def index(request, id):
    connect(settings.MONGOBD_ALIAS)
    if request.method == 'GET':
        todo = Todo.objects(uid=id).first()
        if todo is None:
            return HttpResponse("Instance is not exist")
        else:
            return HttpResponse(json_utils.mongo_to_json(todo), content_type="application/json")

    elif request.method == 'POST' or request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        todo = Todo.objects(uid=id).first()
        if todo is None:
            todo = Todo()
            todo.uid = id

        for key in data:
            setattr(todo, key, data[key])
        todo.save()
        return HttpResponse(json_utils.mongo_to_json(todo), content_type="application/json")

    elif request.method == 'DELETE':
        todo = Todo.objects(uid=id).first()
        if todo is None:
            return HttpResponse("Instance is not exist")
        else:
            todo.delete()
            return HttpResponse("Delete successful")
    else:
        return HttpResponse("Method not support:" + request.method)



@csrf_exempt
def list(request):
    connect(settings.MONGOBD_ALIAS)
    if request.method == 'GET':
        todos = Todo.objects().order_by("index")
        return HttpResponse(json_utils.mongo_to_json(todos), content_type="application/json")

    elif request.method == 'POST' or request.method == 'PUT':
        datas = json.loads(request.body.decode('utf-8'))
        for data in datas:
            id = data["uid"]
            todo = Todo.objects(uid=id).first()
            if todo is None:
                todo = Todo()
                todo.uid = id

            for key in data:
                setattr(todo, key, data[key])
            todo.save()
        return HttpResponse("Update all successful")

    elif request.method == 'DELETE':
        Todo.objects().delete()
        return HttpResponse("Delete all successful")
    else:
        return HttpResponse("Method not support:" + request.method)



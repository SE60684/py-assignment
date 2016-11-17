from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from todo.models import Todo
from django.db import models
from utils import json_utils
import sys
import jwt
import json

from django.core import serializers
from django.shortcuts import render

# Create your views here.



@csrf_exempt
def index(request, id):
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(pk=id)
            return HttpResponse(json_utils.json(todo), content_type="application/json")
        except Todo.DoesNotExist:
            return HttpResponse("Instance is not exist")

    elif request.method == 'POST' or request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))

        try:
            todo = Todo.objects.get(pk=id)
        except Todo.DoesNotExist:
            todo = Todo()
            todo.id = id

        for key in data:
            setattr(todo, key, data[key])
        todo.save()

        return HttpResponse(json_utils.json(todo), content_type="application/json")

    elif request.method == 'DELETE':
        try:
            todo = Todo.objects.get(pk=id)
            todo.delete()
            return HttpResponse("Delete successful")
        except Todo.DoesNotExist:
            return HttpResponse("Instance is not exist")

    else:
        return HttpResponse("Method not support:" + request.method)


@csrf_exempt
def list(request):
    if request.method == 'GET':
        todos = [todo for todo in Todo.objects.all().order_by("index")]
        return HttpResponse(json_utils.json(todos), content_type="application/json")

    elif request.method == 'POST' or request.method == 'PUT':
        datas = json.loads(request.body.decode('utf-8'))
        for data in datas:
            item_id = data["id"]
            try:
                todo = Todo.objects.get(pk=item_id)
            except Todo.DoesNotExist:
                todo = Todo()
                todo.id = item_id

            for key in data:
                setattr(todo, key, data[key])
            todo.save()
        return HttpResponse("Update all successful")

    elif request.method == 'DELETE':
        Todo.objects.all().delete()
        return HttpResponse("Delete all successful")
    else:
        return HttpResponse("Method not support:" + request.method)



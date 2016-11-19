import json
from todo.models import QuerySet
from bson.objectid import ObjectId


def to_dict(entity):
    if isinstance(entity, {}.__class__):
        result = {}
        diction = entity
        for key in diction:
            if not key.startswith("_"):
                result[key] = to_dict(diction[key])
        return result
    elif isinstance(entity, [].__class__):
        result = []
        array = entity
        for item in array:
            result.append(to_dict(item))
        return result
    else:
        if hasattr(entity, '__dict__'):
            entity = entity.__dict__
            return to_dict(entity)
        else:
            return entity


def to_json(entity):
    return json.dumps(to_dict(entity))


def mongo_to_dict(entity):
    if isinstance(entity, QuerySet):
        result = []
        for obj in entity:
            result.append(mongo_to_dict(obj))
        return result
    else:
        result = {}
        fields = entity._data
        for field in fields:
            if not isinstance(entity[field], ObjectId):
                result[field] = entity[field]
        return dict(result)


def mongo_to_json(entity):
    return json.dumps(mongo_to_dict(entity))


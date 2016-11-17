import json as sysjson


def pojo(entity):
    if isinstance(entity, {}.__class__):
        result = {}
        diction = entity
        for key in diction:
            if not key.startswith("_"):
                result[key] = pojo(diction[key])
        return result
    elif isinstance(entity, [].__class__):
        result = []
        array = entity
        for item in array:
            result.append(pojo(item))
        return result
    else:
        if hasattr(entity, '__dict__'):
            entity = entity.__dict__
            return pojo(entity)
        else:
            return entity


def json(entity):
    return sysjson.dumps(pojo(entity))


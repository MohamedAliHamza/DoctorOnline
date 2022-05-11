

def _object_exist(model, **kwargs):
    return model.objects.filter(**kwargs).exists()


def _get_object(model, *args, **kwargs):
    '''If this object exists then return it with specific values from *args using only(), else return None'''
    try:
        obj = model.objects.only(*args).get(**kwargs) # Be careful when using only(), it may cause another query if used in a wrong way!
        return obj
    except model.DoesNotExist:
        return

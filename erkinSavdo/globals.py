from django.conf import settings

def config(request):
    return {
        'title':"Erkin Savdo",
        "current_url":f"{request.path}",
        'languages':settings.LANGUAGES,
        'language_code':settings.LANGUAGE_CODE,
        'LANGUAGE':request.path[1:3],
    }
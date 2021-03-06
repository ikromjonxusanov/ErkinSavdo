from django import template
from erkinSavdoApp.models import *
from django.core.paginator import Paginator
register = template.Library()

# @register.filter(name="kesish")
def kesish(value):
    if len(value) > 50:
        return value[:50]+"..."
    else:
        return value
def ayirish(value, arg):
    return int(value)-int(arg)
def indexList(value, arg):
    return value[int(arg)]
def activeNav(value):
    return value + " active"
def paginatorList(value, arg):

    object = Home.objects.all()
    
    paginator= Paginator(object, 8)
    arg = 8
    objects = paginator.page(value)
    arr = []
    if objects.paginator.num_pages  == value:
        for item in range(value+1-arg, value+objects.paginator.num_pages):
            print("Hello")
            print(item)
            if item > 0 and item < objects.paginator.num_pages:
                if len(arr) != arg:
                    arr.append(item)
                else:
                    pass
        arr.append(value)

    elif objects.paginator.num_pages  > value:
        for item in range(value+1, value+arg):
            if len(arr) != 0:
                if item > 0 and item < objects.paginator.num_pages:
                    if item > objects.paginator.num_pages:
                        for _item in range(value-1, arg, -1):
                            if len(arr) > 4:
                                break
                            else:
                                print('1')
                                arr.append(_item)
                    elif arr[-1] == objects.number:
                        for i in range(1, arg-1):
                            if value-i > 0:
                                print('2')
                                arr.append(value-i)
                    elif len(arr) != arg:
                        print('3')
                        arr.append(item)
                    else:
                        pass
            else:
                arr.append(item)
        arr.append(value)

    # if not 1 in arr:
    #     arr.append(1)
    # if not posts.paginator.num_pages in arr:
    #     arr.append(posts.paginator.num_pages)
    # arr.append(value)
    arr = list(set(arr))
    arr.sort()
    print(arr)
    return arr
def lang(value,arg):
    print(value)
    return value.filter(language=arg)


register.filter('kesish', kesish)
register.filter('ayirish', ayirish)
register.filter('activeNav', activeNav)
register.filter('pa', paginatorList)
register.filter('lang', lang)
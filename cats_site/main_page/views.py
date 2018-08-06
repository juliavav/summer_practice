from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from ipware import get_client_ip
import json
import random

from .models import Cat
from .aero_connection import open_aero, close_aero, check_user_seed


def index(request):
    client_ip, is_routable = get_client_ip(request)
    if client_ip is None:
        print("Unable to get the client's IP address")
    client = open_aero()
    client_seed = check_user_seed(client_ip, client)
    random.seed(client_seed)
    cats_list = list(Cat.objects.all())
    random.shuffle(cats_list)
    cats_list = cats_list[:20]
    context = {'cats_list': cats_list}
    return render(request, 'main_page/cat.html', context)


def new_page(request, end):
    end = int(end)
    begin = end - 20
    client_ip, is_routable = get_client_ip(request)
    if client_ip is None:
        print("Unable to get the client's IP address")
    client = open_aero()
    client_seed = check_user_seed(client_ip, client)
    random.seed(client_seed)
    cats_list = list(Cat.objects.all())
    random.shuffle(cats_list)
    cats_list = cats_list[begin:end]
    cat_json = serializers.serialize('json', cats_list)
    cat_json = json.loads(cat_json)
    cat_json = [x["fields"] for x in cat_json]
    cat_json = json.dumps(cat_json)
    return HttpResponse(cat_json, content_type='application/json')

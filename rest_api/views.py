from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from uuid import uuid4
# Create your views here.


def index(request):
    request_id = uuid4()
    if request.method == 'POST':
        resp = {
            'request_id': request_id,
            'message': 'hello world',
        }
        return JsonResponse(resp)
    else:
        resp = {
            'request_id': request_id,
            'error_message': 'error request method',
        }
        return JsonResponse(status=400, data=resp)
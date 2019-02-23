from django.shortcuts import render
from django.http import JsonResponse
from uuid import uuid4
from django.views.decorators import csrf
# Create your views here.

@csrf.csrf_exempt
def rest_api(request):
    request_id = uuid4()
    if request.method == 'POST':
        resp = {
            'request_id': request_id,
            'message': 'Thanks for your comming!',
        }
        return JsonResponse(resp)
    else:
        resp = {
            'request_id': request_id,
            'error_message': 'Method Not Allowed',
        }
        return JsonResponse(status=405, data=resp)
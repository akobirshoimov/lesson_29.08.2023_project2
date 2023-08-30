from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def all_info(request,laptop_id):
    return HttpResponse('all info!')

def detail(request,laptop_id,phone_id):
    try:
        laptop,phone = laptop.objects.get(id=laptop_id),phone.objects.get(id=phone_id)
    
        return HttpResponse(f'you are loking at laptop_id:{laptop_id},laptop_id:{phone_id}')
    except phone.DoesNotExist:
        return HttpResponse(f'{laptop_id},{phone_id} not found')

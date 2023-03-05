import imp
from select import select
from django.shortcuts import render
from django.http import JsonResponse
from App.models import Employee
from App.serializer import Empserializer


def Emp(request):
    Emp=Employee.objects.all()
    serilizer=Empserializer(Emp, many=True)
    
    return JsonResponse(serilizer.data, safe=False)
   



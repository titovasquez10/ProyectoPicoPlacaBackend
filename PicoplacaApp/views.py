from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from PicoplacaApp.models import Ciudades, Picoplaca
from PicoplacaApp.serializers import CiudadSerializer, PicoplacaSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def ciudadApi(request,id=0):
    if request.method=='GET':
        ciudades = Ciudades.objects.all()
        ciudades_serializer = CiudadSerializer(ciudades, many=True)
        return JsonResponse(ciudades_serializer.data, safe=False)

    elif request.method=='POST':
        ciudades_data=JSONParser().parse(request)
        ciudades_serializer = CiudadSerializer(data=ciudades_data)
        if ciudades_serializer.is_valid():
            ciudades_serializer.save()
            return JsonResponse("Added Sucessfully!!!" , safe=False)
        return JsonResponse("Failed to Add",safe=False)
    
    elif request.method=='PUT':
        ciudades_data = JSONParser().parse(request)
        ciudades=Ciudades.objects.get(CiudadId=ciudades_data['CiudadId'])
        ciudades_serializer=CiudadSerializer(ciudades,data=ciudades_data)
        if ciudades_serializer.is_valid():
            ciudades_serializer.save()
            return JsonResponse("Updated Succesfully!!!", safe=False)
        return JsonResponse("Falid to Update.", safe=False)

    elif request.method=='DELETE':
        ciudades=Ciudades.objects.get(CiudadId=id)
        ciudades.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

@csrf_exempt
def picoplacaApi(request,id=0):
    if request.method=='GET':
        picoplaca = Picoplaca.objects.all()
        picoplaca_serializer = PicoplacaSerializer(picoplaca, many=True)
        return JsonResponse(picoplaca_serializer.data, safe=False)

    elif request.method=='POST':
        picoplaca_data=JSONParser().parse(request)
        picoplaca_serializer = PicoplacaSerializer(data=picoplaca_data)
        if picoplaca_serializer.is_valid():
            picoplaca_serializer.save()
            return JsonResponse("Added Sucessfully!!!" , safe=False)
        return JsonResponse("Failed to Add",safe=False)
    
    elif request.method=='PUT':
        picoplaca_data = JSONParser().parse(request)
        picoplaca=Picoplaca.objects.get(DigitoplacaId=picoplaca_data['DigitoplacaId'])
        picoplaca_serializer=PicoplacaSerializer(picoplaca,data=picoplaca_data)
        if picoplaca_serializer.is_valid():
            picoplaca_serializer.save()
            return JsonResponse("Updated Succesfully!!!", safe=False)
        return JsonResponse("Falid to Update.", safe=False)

    elif request.method=='DELETE':
        picoplaca=Picoplaca.objects.get(DigitoplacaId=id)
        picoplaca.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

# ---------------------------------------------------------------

@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)


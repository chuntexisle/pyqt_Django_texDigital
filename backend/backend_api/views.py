from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import TexileAppTestqt, TexileAppReleasedLots
from .serializers import TexileAppTestqtSerializer, TexileAppReleasedLotsSerializer

# Create your views here.
@csrf_exempt
def releasedlots_list(request):
    if request.method == 'GET':
        lots = TexileAppReleasedLots.objects.all()
        serializer = TexileAppReleasedLotsSerializer(lots, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TexileAppReleasedLotsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def releasedlots_detail(request, pk):
    print("*************")
    print(request)
    
    print(pk)
    try:
        print("XXXXXXXXXXXXXXXXXX")
        lot = TexileAppReleasedLots.objects.get(pk=pk)
        print("YYYYYYYYYYYYYYY")
        print('lot is ', lot)
    except lot.DoesNotExist:
        print('EEEEEEEEEEEEEEEE')
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TexileAppReleasedLotsSerializer(lot)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        print("KKKKKKKKKKKKKK")
        data = JSONParser().parse(request)
        print(data)
        serializer = TexileAppReleasedLotsSerializer(lot, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        print("PPPPPPPPPPPPPPPP")
        data = JSONParser().parse(request)
        print(data)
        serializer = TexileAppReleasedLotsSerializer(lot, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        lot.delete()
        return HttpResponse(status=204)

class ProcessingListView(ListView):
    model = TexileAppTestqt

   
@csrf_exempt
def processing_detail(request, pk):
    try:
        processing = TexileAppTestqt.objects.get(pk=pk)
    except processing.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TexileAppTestqtSerializer(processing)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TexileAppTestqtSerializer(processing, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TexileAppTestqtSerializer(processing, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        processing.delete()
        return HttpResponse(status=204)



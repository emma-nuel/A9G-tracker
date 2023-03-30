from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import MyTracker
from .serializer import MyTrackerDataSerializer
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.
class LocationData(APIView):
    def get(self, request, format=None):
        location  = MyTracker.objects.all().last()
        serializer = MyTrackerDataSerializer(location)
        return HttpResponse(json.dumps(serializer.data), content_type='application/json')
    
    def post(self, request, format=None):
        serializer = MyTrackerDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.core import serializers
from django.shortcuts import render
import json
from rest_framework import views, status
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Provider, Availabilities
from .serializers import ProviderSerializer
# Create your views here.



class ProviderView(views.APIView):
    def get(self, request):
        min_score = request.GET.get('minScore', None)
        date = request.GET.get('date', None)
        speciality = request.GET.get('speciality', None)
        print(not speciality)
        if not speciality or not date or not speciality:
            return HttpResponseBadRequest('<h1>Error in query</h1>')

        providers = Provider.objects.filter(score__gte=min_score)\
            .filter(availableDates__to_time__gte=date)\
            .filter( availableDates__from_time__lte=date)\
            .filter(specialities__type__iexact=speciality)
        values = list(set([p.name for p in providers]))
        print(values)
        return Response(values)

    # def post(self, request):
    #     serializer = BookSerializer(data=request.data)
    #     print(serializer, serializer.is_valid())
    #     if serializer.is_valid():
    #         avails = Availabilities.objects.all() #filter(from_time__gte=serializer.data['date'], to_time_lte=serializer.data['date'])
    #         print(avails)
    #
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
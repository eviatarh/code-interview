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

        if not speciality or not date or not min_score:
            print(speciality, date, min_score)
            return HttpResponseBadRequest('<h1>Error in query</h1>')

        providers = Provider.objects.filter(score__gte=min_score)\
            .filter(availabilities__to_time__gte=date)\
            .filter(availabilities__from_time__lte=date)\
            .filter(specialities__type__iexact=speciality).order_by('-score').distinct()
        print(providers)
        values = [p.name for p in providers]
        print(values)
        return Response(values)


    def post(self, request):
        req_dict = json.loads(request.body)
        params = list(req_dict.keys())
        if "name" not in params or "date" not in params:
            return HttpResponseBadRequest('<h1>Error in query</h1>')

        name = req_dict['name']
        date = req_dict['date']
        try:
            res = Provider.objects.filter(name=name) \
                .filter(availabilities__to_time__gte=date) \
                .filter(availabilities__from_time__lte=date)
            if res:
                return HttpResponse('<h1>Provider available</h1>')
        except Exception as e:
            res = []

        print(res)
        return HttpResponseBadRequest('<h1>Error in query</h1>')
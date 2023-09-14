from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from unidecode import unidecode
from rest_framework.decorators import api_view
from selenium import webdriver
from app.models import City, SunSet
import random
import time
import requests
import re
from selenium.webdriver.common.by import By
from django.db.models import Q
from geopy.geocoders import Nominatim
import math
from geopy.distance import geodesic
from app.serializer import SunSetSerializer


@api_view(['GET', 'POST'])
def sun_set(request):
    
    if request.method == 'GET':
        # Access query parameters from request.GET for GET requests
        city = request.GET.get('city')  # Default to 'Tel Aviv' if not provided
        lon = request.GET.get('longitude')
        lat = request.GET.get('latitude')
        radius = request.GET.get('radius', 10)  # Default to 10 if not provided
    elif request.method == 'POST':
        # Access JSON data from request.data for POST requests
        city = request.data.get('city')  # Default to 'Tel Aviv' if not provided
        lon = request.data.get('longitude')
        lat = request.data.get('latitude')
        radius = request.data.get('radius', 10)
    # normalized_city_name = unidecode(city)
    # normalized_city_name = normalized_city_name.strip()
    # city_objs = City.objects.filter(Q(city__iexact=normalized_city_name) | Q(city__icontains=normalized_city_name)).first()
    # if city_objs:
    #     # sunset_attractions=SunSet.objects.filter(city_id=city_objs)
    center_point = (lat, lon)

    sunset_attractions = [
        obj for obj in SunSet.objects.all() if
        geodesic(center_point, (obj.latitude, obj.longitude)).km <= radius
    ]
    serializer = SunSetSerializer(sunset_attractions, many=True)
    
    return Response(serializer.data, status=200)





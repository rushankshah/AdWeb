from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import AdvertisementForm
from .models import Advertisement
import requests
import random
import math
import json
# Create your views here.


def index(request):
    Advertisements = Advertisement.objects.all()
    return render(request, 'adtool/index.html', context={'Advertisements': Advertisements})


def upload(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AdvertisementForm()
    return render(request, 'adtool/upload.html', context={'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


@api_view(['GET', 'POST'])
def api(request):

    try:
        random_pk = Advertisement.objects.count()*random.random()
        random_pk = math.floor(random_pk) + 1
        random_advertisement = Advertisement.objects.get(pk=random_pk)
        # Retrieve advertisement image from Database here and send it as json
        advertisement_site = "http://127.0.0.1:3000/site/"
        advertisement_image = 'http://127.0.0.1:3000' + random_advertisement.ad_image.url
        advertisement_html = f"<a href=\"{advertisement_site}\"><img src=\"{advertisement_image}\"></a>"
        return JsonResponse(advertisement_html, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

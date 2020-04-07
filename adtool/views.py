from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.core import serializers
from .forms import AdvertisementForm
from .models import Advertisement

# For API
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from adtool.advertisement_api import AdvertisementAPI
# Create your views here.

# testing
import base64
from PIL import Image
from io import BytesIO


class AdvertisementListView(LoginRequiredMixin, ListView):
    model = Advertisement
    template_name = 'adtool/home.html'
    context_object_name = 'Advertisements'
    # ordering = ['-id']

    def get_queryset(self):
        return Advertisement.objects.filter(user=self.request.user).order_by('-id')


class AdvertisementDetailView(LoginRequiredMixin, UserPassesTestMixin,  DetailView):
    model = Advertisement

    def test_func(self):
        advertisement = self.get_object()
        if self.request.user == advertisement.user:
            return True
        return False


class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    fields = fields = ['name', 'ad_image', 'url_link', 'genre', 'category']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AdvertisementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Advertisement
    fields = fields = ['name', 'ad_image', 'url_link', 'genre', 'category']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        advertisement = self.get_object()
        if self.request.user == advertisement.user:
            return True
        return False


class AdvertisementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Advertisement
    success_url = '/site'

    def test_func(self):
        advertisement = self.get_object()
        if self.request.user == advertisement.user:
            return True
        return False


@login_required
def dashboard(request):
    ads = Advertisement.objects.filter(user=request.user)
    ads = serializers.serialize('json', ads)

    context = {
        'ads': ads,
    }
    return render(request, 'adtool/dashboard.html', context)


@api_view(['GET', 'POST'])
def api(request, user_key):
    try:
        advertisementapi = AdvertisementAPI(request, Advertisement)
        advertisement_html = advertisementapi.get_advertisement(user_key)
        return JsonResponse(advertisement_html, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def ad_redir(self, pk):
    ad = Advertisement.objects.get(pk=pk)
    ad.clicks += 1
    ad.save()

    return redirect(str(Advertisement.objects.get(pk=pk).url_link))

# index, upload, success are redundant


def index(request):
    Advertisements_by_current_user = Advertisement.objects.filter(
        user=request.user)
    return render(request, 'adtool/home.html', context={'Advertisements': Advertisements_by_current_user})


def upload(request):
    if request.method == 'POST':
        form = AdvertisementForm(
            user=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AdvertisementForm()
    return render(request, 'adtool/upload.html', context={'form': form})


def success(request):
    img_path = Advertisement.objects.get(pk=4).ad_image.path
    image = Image.open(img_path)
    img_format = image.format.lower()
    with open(img_path, 'rb') as f:
        img = base64.b64encode(f.read()).decode('utf-8')

    return render(request, "adtool/test.html", {'img': img, 'img_format': img_format})

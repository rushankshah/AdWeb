from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.core import serializers
from .forms import AdvertisementForm
from .models import Advertisement, AdvertisementLog

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
from addisplay.models import Website


class AdvertisementListView(LoginRequiredMixin, ListView):
    model = Advertisement
    template_name = 'adtool/home.html'
    context_object_name = 'Advertisements'
    # ordering = ['-id']
    paginate_by = 5

    def get_queryset(self):
        return Advertisement.objects.filter(user=self.request.user).order_by('-id')


class AdvertisementDetailView(LoginRequiredMixin, UserPassesTestMixin,  DetailView):
    model = Advertisement

    def test_func(self):
        advertisement = self.get_object()
        if self.request.user == advertisement.user:
            return True
        return False

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        log = serializers.serialize('json', self.get_object().advertisementlog_set.all())
        context['click_log'] = log
        return context


class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    fields = ['name', 'size', 'image', 'url_link', 'category']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AdvertisementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Advertisement
    fields = ['name', 'image', 'url_link', 'size', 'category']

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
    success_url = '/'

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


def api(request, size, user_key):
    try:
        advertisementapi = AdvertisementAPI(request, Advertisement, size)
        advertisement_html = advertisementapi.get_advertisement(user_key)
        return JsonResponse(advertisement_html, safe=False)
    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    


def ad_redir(self, pk, site_pk):
    try:
        w = Website.objects.get(pk=site_pk)
        ad = Advertisement.objects.get(pk=pk)
        ad.clicks += 1
        ad.save()
        AdvertisementLog.objects.create(ad=ad, site=w)
        return redirect(str(Advertisement.objects.get(pk=pk).url_link))
    except Exception as e:
        return Http404()


def landing(request):
    return render(request, 'adtool/landing.html')

def about(request):
    return render(request, 'adtool/about.html')

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
    img_path = Advertisement.objects.get(pk=4).image.path
    image = Image.open(img_path)
    img_format = image.format.lower()
    with open(img_path, 'rb') as f:
        img = base64.b64encode(f.read()).decode('utf-8')

    return render(request, "adtool/test.html", {'img': img, 'img_format': img_format})

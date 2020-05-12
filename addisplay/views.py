from django.shortcuts import render, redirect
from .models import AdvertisementClient, Website
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

@login_required
def register_website(request):
    ac_check = AdvertisementClient.objects.filter(user=request.user)
    if ac_check.exists():
        if request.method == 'GET':
            w = Website.objects.filter(client=ac_check.first())
            return render(request, 'addisplay/website_key.html', context={'websites': w})
        elif request.method == 'POST':
                if request.POST['btn'] == 'add':
                    Website.objects.create(client=ac_check.first(), url=request.POST['website-url']).save()
                elif request.POST['btn'] == 'delete':
                    try:
                        Website.objects.get(client=ac_check.first(), url=request.POST['website-url']).delete()
                    except Exception as e:
                        pass

                return redirect('adclient:register_website')
    else:
        if request.method == 'POST':
            ac = AdvertisementClient.objects.create(user=request.user)
            Website.objects.create(client=ac, url=request.POST['website-url']).save()
            messages.success(request, "Your account has been updated, now you can display ads on your website")
            return redirect('adclient:register_website')

        elif request.method == 'GET':
            return render(request, 'addisplay/adclient_confirmation.html')
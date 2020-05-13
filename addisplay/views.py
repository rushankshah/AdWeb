from django.shortcuts import render, redirect
from .models import Website
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

@login_required
def register_website(request):
    user = request.user
    if user.profile.is_adclient:
        if request.method == 'GET':
            w = Website.objects.filter(user=user)
            return render(request, 'addisplay/website_key.html', context={'websites': w})
        elif request.method == 'POST':
                if request.POST['btn'] == 'add':
                    Website.objects.create(user=user, url=request.POST['website-url']).save()
                elif request.POST['btn'] == 'delete':
                    try:
                        Website.objects.get(user=user, url=request.POST['website-url']).delete()
                    except Exception as e:
                        pass

                return redirect('adclient:register_website')
    else:
        if request.method == 'POST':
            u_p = user.profile
            u_p.is_adclient = True
            u_p.save()
            Website.objects.create(user=user, url=request.POST['website-url']).save()
            messages.success(request, "Your account has been updated, now you can display ads on your website")
            return redirect('adclient:register_website')

        elif request.method == 'GET':
            return render(request, 'addisplay/adclient_confirmation.html')
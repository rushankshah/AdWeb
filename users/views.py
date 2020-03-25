from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('users:login')
    else:
        register_form = UserRegistrationForm()
    return render(request, 'users/register.html', context={'registerform': register_form})


@login_required(login_url='users:login')
def profile(request):
    return render(request, 'users/profile.html')

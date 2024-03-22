from django.urls import reverse
from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, "users/login.html", context=context)


def registration(request):
    return render(request, "users/registration.html")

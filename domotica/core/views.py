from django.shortcuts import render, redirect
from .models import data_login
from .forms import LoginForm
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def home(request): 
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LoginForm()
    context = {
        'form':form,
    }
    return render(request, "core/index.html", context )

from django.shortcuts import render

from .models import User


def home_view(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'home.html', context) 

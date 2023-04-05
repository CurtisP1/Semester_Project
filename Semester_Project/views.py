from django.contrib import auth
from django.shortcuts import render


def index(request):
    data = ""
    user_details = auth.get_user(request)
    profile_picture = 'user_placeholder.svg'
    context = {
        'data': data,
        'profile_picture': profile_picture
    }
    return render(request, 'index.html', context)

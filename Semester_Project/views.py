from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        profile_picture = request.user.profile.profile_picture
    else:
        profile_picture = "static/images/user_placeholder.png"

    context = {
        'profile_picture': profile_picture
    }
    return render(request, 'index.html', context)

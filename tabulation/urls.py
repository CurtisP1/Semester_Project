#  Copyright (c) 2023.
#  Created by Jan Boer for SEPT 4IT3
#  I Jan Boer, 0862551 certify that this material is my original work.
#  No other person's work has been used without due acknowledgement. I have also not made my work available to anyone else without it being acknowledged.
from django.urls import path

from . import views

app_name = 'tabulation'
urlpatterns = [
    path('', views.index, name='index'),
    path("sinewave/", views.sine_wave, name='sine_wave'),
]

#  Copyright (c) 2023.
#  Created by Jan Boer for SEPT 4IT3
#  I Jan Boer, 0862551 certify that this material is my original work.
#  No other person's work has been used without due acknowledgement. I have also not made my work available to anyone else without it being acknowledged.

import numpy as np
from django.shortcuts import render


def index(request):
    data = []
    values = np.linspace(0, 1000, 1000)
    values = np.sin(values * np.pi ** 2)
    FFT = fft_sine(values)
    for i in range(len(values)):
        data.append({'label': i, 'value': values[i], "fft": FFT[i]})

    if (request.method == "GET"):
        pass
    gets = {"fft_hide": request.GET.get('fft_hide')}
    debug = request.method
    context = {
        "data" : data,
        "gets" : gets,
        "debug": debug
    }
    page = 'tabulation/sinewave.html'
    return render(request, page, context)


def sine_wave(request):
    data = []
    values = np.linspace(0, 1000, 1000)
    values = np.sin(values * np.pi ** 2)
    FFT = fft_sine(values)
    for i in range(len(values)):
        data.append({'label': i, 'value': values[i], "fft": FFT[i]})

    gets = {"fft_hide": request.GET.get('fft_hide')}
    debug = request.method
    context = {
        "data" : data,
        "gets" : gets,
        "debug": debug
    }
    page = 'tabulation/sinewave.html'
    return render(request, page, context)


def fft_sine(data):
    data = np.fft.fft(data)
    return data

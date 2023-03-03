#  Copyright (c) 2023.
#  Created by Jan Boer for SEPT 4IT3
#  I Jan Boer, 0862551 certify that this material is my original work.
#  No other person's work has been used without due acknowledgement. I have also not made my work available to anyone else without it being acknowledged.
import json

import numpy as np
from django.shortcuts import render


class SineWaveData:
    values: int = []
    labels: str = []

    def __init__(self):
        labels = np.linspace(0, 1000, 1000, dtype=int)
        values = np.sin(labels * np.pi ** 2)
        self.values = json.dumps(values.tolist())
        self.labels = json.dumps(labels.tolist())


def index(request):
    template = 'dashboard/sinewave.html'
    data = SineWaveData()
    context = {
        "data": data,
    }
    return render(request, template, context)


def sinewave(request):
    template = 'dashboard/sinewave.html'
    data = SineWaveData
    context = {
        "data": data,
    }
    return render(request, template, context)
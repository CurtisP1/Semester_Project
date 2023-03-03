#  Copyright (c) 2023.
#  Created by Jan Boer for SEPT 4IT3
#  I Jan Boer, 0862551 certify that this material is my original work.
#  No other person's work has been used without due acknowledgement. I have also not made my work available to anyone else without it being acknowledged.

from django.db import models


# Create your models here.
class SineData(models.Model):
    value = models.DecimalField(decimal_places=32, max_digits=32)
    label = models.TimeField(auto_now=True)

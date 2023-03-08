"""Semester_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#  Copyright (c) 2023.
#  Created by Curtis Poon for SEPT 4IT3.
#
#  I have not shared my code with anyone without the required consent and annotations being present in their documentation. I have also ensured that all functions are referenced from the location that I sourced them from.
#


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
                  path('', views.index, name='index.html'),
                  path("admin/", admin.site.urls),
                  path("dashboard/", include('dashboard.urls', namespace='dashboard')),
                  path('account/', include('django.contrib.auth.urls')),
                  path("tabulation/", include('tabulation.urls', namespace='tabulation'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

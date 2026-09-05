"""
URL configuration for concert project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from ticketsales.views import (
    concert_list_view,
    time_list_view,
    concert_details_view,
    location_list_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ticketsales/concert/list", concert_list_view),
    path("ticketsales/location/list", location_list_view),
    path("ticketsales/time/list", time_list_view),
    path("ticketsales/concert/<int:concert_id>", concert_details_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

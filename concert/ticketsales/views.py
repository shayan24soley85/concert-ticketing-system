from django.shortcuts import render
from ticketsales.models import ConcertModel
from ticketsales.models import LocationModel


# Create your views here.
def concert_list_view(request):
    concerts = ConcertModel.objects.all()
    context = {
        "concert_list": concerts,
        "concert_count": concerts.count(),
    }

    return render(request, "ticketsales/concert_list.html", context)


def location_list_view(request):
    locations = LocationModel.objects.all()
    context = {"location_list": locations}

    return render(request, "ticketsales/location_list.html", context)

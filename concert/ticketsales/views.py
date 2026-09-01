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


def concert_details_view(request, concert_id):
    concert = ConcertModel.objects.get(pk=concert_id)
    context = {"concert_details": concert}
    return render(request, "ticketsales/concert_details.html", context)

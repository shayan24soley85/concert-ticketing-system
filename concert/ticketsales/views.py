from django.shortcuts import render
from ticketsales.models import ConcertModel


# Create your views here.
def concert_list_view(request):
    concerts = ConcertModel.objects.all()
    context = {
        "concert_list": concerts,
        "concert_count": concerts.count(),
    }

    return render(request, "ticketsales/concert_list.html", context)

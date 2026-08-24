from django.shortcuts import render
from django.http import HttpResponse
from ticketsales.models import ConcertModel


# Create your views here.
def concert_list_view(request):
    concerts = ConcertModel.objects.all()
    return HttpResponse(concerts)

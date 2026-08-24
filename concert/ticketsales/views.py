from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def concert_list_view(request):
    return HttpResponse("لیست کنسرت های موجود")

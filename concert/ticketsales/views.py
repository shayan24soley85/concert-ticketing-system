from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def concert_list_view(request):
    return HttpRequest("لیست کنسرت های موجود")

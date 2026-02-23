from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def slash_view(request) -> HttpResponse:
    print(request.headers['Cookie'])
    return HttpResponse('It works!')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dash(request):
    return HttpResponse("Hello Dashboard!")
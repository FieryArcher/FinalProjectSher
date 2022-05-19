from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# def index(request):
#     return render(request, 'courier/index.html')


def index(request):
    return HttpResponse('<h1>hello Telzhan</h1>')



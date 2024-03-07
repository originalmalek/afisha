from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def first_page(request):
    return render(request, 'where/index.html')

from django.shortcuts import render
from django.conf import settings

# Create your views here.


def view(request):

    a = settings.MY_SETTINGS['item']['subitem']

    print(a)

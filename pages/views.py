import imp
from django.shortcuts import render

# import Http Responses to return Http Response object to user
from django.http import HttpResponse


# Create your views here.
# Setting up Home page View
def homePageView(request):
    # return Http Response object to user
    return HttpResponse("Hello Python Nice to Meet you")

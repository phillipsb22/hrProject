from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#import inspect,os


def index(request):
    return HttpResponse("Test http response")

# Create your views here.

def test(request):
	return HttpResponse("Gets to view 2 to make sure")

def login(request):
    #return HttpResponse(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
    template = loader.get_template('leave/login.html')
    return HttpResponse(template.render(request))



from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.

"""
class IndexView(TemplateView):
    
    #template_name = 'index.html'

    def get(self, request):
        return HttpResponse('hello world')
"""

def index(request):
    return HttpResponse("hello world")

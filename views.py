from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    return HttpResponse('Hello World，Come on man，You block me several days，what TM can i say?')
# Create your views here.

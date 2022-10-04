from django.http import HttpRequest, HttpResponse, Http404

def hello(request:HttpRequest):
    return HttpResponse("Hello")
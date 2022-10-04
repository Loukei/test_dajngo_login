from multiprocessing import context
from django.http import HttpRequest, HttpResponse, Http404
from django.template import loader as template_loader, TemplateDoesNotExist

def hello(request:HttpRequest):
    "Simply show hello for test"
    return HttpResponse("Hello")

def index(request:HttpRequest):
    try:
        template = template_loader.get_template(template_name="mysite/index.html")
        context:dict = {}
    except TemplateDoesNotExist:
        raise Http404("Index page does not found")
    return HttpResponse(content=template.render(context=context,request=request))
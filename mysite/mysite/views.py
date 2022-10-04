from multiprocessing import context
from django.http import HttpRequest, HttpResponse, Http404
from django.template import loader as template_loader, TemplateDoesNotExist
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

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

def profile(request:HttpRequest, username:str):
    """
    Show user profile in page
    #TODO: add login control
    """
    # check user
    current_user:User = request.user
    if (current_user.get_username() == username):
        t = template_loader.get_template(template_name='mysite/profile.html')
        context:dict = {}
        return HttpResponse(content=t.render(context=context,request=request))
    else:
        raise Http404(f"you don't have permission to this page.")
    
class CustomLoginView(LoginView):
    template_name: str = "mysite/login.html"

    def get_success_url(self) -> str:
        "Override function to redirect"
        return self.get_redirect_url() or reverse(viewname=profile, kwargs={"username": self.request.user.username})
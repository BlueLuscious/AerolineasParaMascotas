from django.http import HttpResponse
from django.views import View
from django.template import loader

template = loader.get_template("pages/index.html")


class IndexView(View):
    
    def get(self, request):
        return HttpResponse(template.render(None, request))
    
    def post(self, request):
        return HttpResponse(template.render(None, request))
    
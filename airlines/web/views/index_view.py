from django.http import HttpResponse
from django.views import View
from django.template import loader


class IndexView(View):
    
    def get(self, request):
        template = loader.get_template("pages/index.html")
        return HttpResponse(template.render(None, request))
    
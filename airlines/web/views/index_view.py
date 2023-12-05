from django.http import HttpResponse
# from django.shortcuts import redirect
from django.views import View
from django.template import loader

from destination.services import DestinationServices

template = loader.get_template('index.html')

class IndexView(View):
    def get(self, request):
        context = DestinationServices.get_context()
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        pass
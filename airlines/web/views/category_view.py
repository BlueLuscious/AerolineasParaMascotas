from django.http import HttpResponse
# from django.shortcuts import redirect
from django.views import View
from django.template import loader

from destination.services import DestinationServices

template = loader.get_template('Razas.html')

class CategoryView(View):
    def get(self, request):
        context=[]
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        return HttpResponse(template.render(None, request))
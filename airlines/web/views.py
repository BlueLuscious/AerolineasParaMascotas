from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
class IndexView(View):
    
    def get(self, request): 
        return render(request, 'index.html')
    
    def post(self, request):
        pass


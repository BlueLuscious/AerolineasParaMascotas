from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views import View
from store.models import ProductModel
from config.models import ConfigModel

class QuotationView(View):
    
    def get(self, request: HttpRequest) -> HttpResponse:
        template = loader.get_template("pages/quotations/quotation.html")
        products = ProductModel.objects.all()
        config = ConfigModel.objects.get(active=True)
        context = {
            'products': products,
            'config': config,
            
        }
        return HttpResponse(template.render(context, request))
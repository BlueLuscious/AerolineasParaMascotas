from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views import View
from store.models import ProductModel

class QuotationView(View):
    
    def get(self, request: HttpRequest) -> HttpResponse:
        template = loader.get_template("pages/quotations/quotation.html")
        products = ProductModel.objects.all()
        context = {
            'products': products
        }
        return HttpResponse(template.render(context, request))
from django.http import HttpResponse
from django.views import View
from django.template import loader
from app.dtos.destination_o import DestinationO
from config.models.models import ConfigModel
from review.models import ReviewModel
from store.models import ProductModel
from web.mocks.destinations_mock import DestinationMock
from web.mocks.faqs_mock import mock_faqs


class IndexView(View):
    
    def get(self, request):
        template = loader.get_template("pages/index.html")

        products = ProductModel.objects.all()
        config = ConfigModel.objects.get(active=True)

        DestinationMock().mock_destinations()
        destinations = DestinationO.all()

        context = dict(
            reviews=ReviewModel.objects.filter().order_by("-created_at")[:6],
            products=products,
            config=config,
            destinations=destinations,
            faqs=mock_faqs(),
        )
        return HttpResponse(template.render(context, request))
    
from django.http import HttpResponse
from django.views import View
from django.template import loader
from config.models.models import ConfigModel
from review.models import ReviewModel
from store.models import ProductModel
from web.dtos.destination_card_o import DestinationCardO
from web.mocks.destinations_mock import DestinationMock


class IndexView(View):
    
    def get(self, request):
        template = loader.get_template("pages/index.html")

        products = ProductModel.objects.all()
        config = ConfigModel.objects.get(active=True)

        DestinationMock().mock_destinations()
        destinations = DestinationCardO.all()

        context = dict(
            reviews=ReviewModel.objects.filter().order_by("-created_at")[:6],
            products=products,
            config=config,
            destinations=destinations,
        )
        return HttpResponse(template.render(context, request))
    
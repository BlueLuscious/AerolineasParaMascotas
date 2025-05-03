from django.http import HttpResponse
from django.views import View
from django.template import loader
from config.models.models import ConfigModel
from review.models import ReviewModel
from store.models import ProductModel
from web.mocks.destinations_mock import DestinationMock


class IndexView(View):
    
    def get(self, request):
        template = loader.get_template("pages/index.html")

        products = ProductModel.objects.all()
        config = ConfigModel.objects.get(active=True)

        destination_mock = DestinationMock()
        european_destinations = destination_mock.mock_european_destinations()
        american_destinations = destination_mock.mock_american_destinations()
        north_american_destinations = destination_mock.mock_north_american_destinations()
        exotic_destinations = destination_mock.mock_exotic_destinations()

        context = dict(
            reviews=ReviewModel.objects.filter().order_by("-created_at")[:6],
            products=products,
            config=config,
            european_destinations=european_destinations,
            american_destinations=american_destinations,
            north_american_destinations=north_american_destinations,
            exotic_destinations=exotic_destinations,
        )
        return HttpResponse(template.render(context, request))
    
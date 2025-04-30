from django.http import HttpResponse
from django.views import View
from django.template import loader
from review.models import ReviewModel
from web.mocks.destinations_mock import mock_european_destinations


class IndexView(View):
    
    def get(self, request):
        template = loader.get_template("pages/index.html")

        european_destinations = mock_european_destinations()

        context = dict(
            reviews=ReviewModel.objects.filter().order_by("-created_at")[:6],
            european_destinations=european_destinations,
        )
        return HttpResponse(template.render(context, request))
    
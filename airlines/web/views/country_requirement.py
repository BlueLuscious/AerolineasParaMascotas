from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views import View


class CountryRequirementView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        template = loader.get_template("pages/before-fly/country-requirement.html")
        return HttpResponse(template.render(None, request))
    
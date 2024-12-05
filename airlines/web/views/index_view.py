from django.http import HttpResponse
from django.views import View
from django.template import loader
from review.models import ReviewModel


class IndexView(View):
    
    def get(self, request):
        template = loader.get_template("pages/index.html")
        # context = {
        #     "reviews": ReviewModel.objects.all().order_by("-created_at")[:6]
        # }
        return HttpResponse(template.render(None, request))
    
import logging
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import View
from django_q.tasks import async_task
from app.dtos.email_dto import EmailDataDTO
from app.utils.email_service import EmailService

logger = logging.getLogger(__name__)


class QuotationView(View):

    def post(self, request: HttpRequest) -> HttpResponse:
        if request.POST.get('honeypot'):
            logger.warning("Honeypot field filled, possible bot detected.")
            return HttpResponse("Error: Bot detected", status=400)

        try:
            email_data = EmailDataDTO().from_request(request)
            async_task(EmailService(email_data).send_email_with_template)
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            return HttpResponse("Error sending email", status=500)

        return redirect('index')
    
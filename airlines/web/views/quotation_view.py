import json
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views import View
from store.models import ProductModel
from config.models import ConfigModel
from django.core.mail import send_mail
from django.shortcuts import redirect
from django_q.tasks import async_task
import logging

logger = logging.getLogger(__name__)

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

    def post(self, request: HttpRequest) -> HttpResponse:
        if request.POST.get('honeypot'):
            logger.warning("Honeypot field filled, possible bot detected.")
            return HttpResponse("Error: Bot detected", status=400)

        config = ConfigModel.objects.get(active=True)
        email_contact = config.email_contact if config else 'default@example.com'

        owner_name = request.POST.get('owner_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pet_name = request.POST.get('pet_name')
        pet_age = request.POST.get('pet_age')
        pet_weight = request.POST.get('pet_weight')
        pet_breed = request.POST.get('pet_breed')
        pet_photo = request.FILES.get('pet_photo')
        travel_date = request.POST.get('travel_date')
        origin_city = request.POST.get('origin_city')
        destination_city = request.POST.get('destination_city')
        comments = request.POST.get('comments')
        selected_products = request.POST.getlist('selected_products', [])
        
        subject = 'Nueva Solicitud de Cotización'
        message = f"""
        Nombre del propietario: {owner_name}
        Email: {email}
        Teléfono: {phone}
        Foto de la mascota: {pet_photo}
        Nombre de la mascota: {pet_name}
        Edad de la mascota: {pet_age}
        Peso de la mascota: {pet_weight}
        Raza de la mascota: {pet_breed}
        Fecha del viaje: {travel_date}
        Ciudad de Origen: {origin_city}
        Ciudad de Destino: {destination_city}
        Comentarios: {comments}
        Productos seleccionados: {selected_products}
        """

        try:
            async_task(send_mail, subject, message, email, [email_contact])
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            return HttpResponse("Error sending email", status=500)

        return redirect('index')
    
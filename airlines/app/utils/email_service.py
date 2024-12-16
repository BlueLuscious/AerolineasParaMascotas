import json, logging
from email.mime.image import MIMEImage
from premailer import transform
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from app.dtos.email_dto import EmailDataDTO
from app.dtos.product_dto import ProductDTO
from config.models.models import ConfigModel
from store.models import ProductModel

logger = logging.getLogger(__name__)


class EmailService:

    """ Servicio de envio de mails. """

    def __init__(self, email_data: EmailDataDTO) -> None:

        """ Inicializador de EmailService. """
        
        self.config = ConfigModel.objects.get(active=True)
        self.email_contact: str = self.config.email_contact if self.config else "default@example.com"
        self.email_data = email_data


    def send_email_with_template(self, subject: str = "Nueva Solicitud de Cotización") -> None:

        """
        Envia un mail con un template personalizado.

        Args:
            data (dict): Diccionario con los datos de la consulta.
            subject (str): Asunto.
        """

        msg = EmailMultiAlternatives(subject, None, self.email_data.email, [self.email_contact])
        msg.mixed_subtype = "related"

        # Carga imagen en memoria --> Input File
        uploaded_file: InMemoryUploadedFile = self.email_data.pet_photo
        if uploaded_file:
            mime_image = MIMEImage(uploaded_file.read(), _subtype=uploaded_file.content_type.split('/')[-1])
            cid = "uploaded_image_cid"
            mime_image.add_header("Content-ID", f"<{cid}>")
            mime_image.add_header("Content-Disposition", "inline", filename=uploaded_file.name)
            msg.attach(mime_image)
            self.email_data.image_cid = cid

        # Carga imagenes de los productos
        for index, product in enumerate(self.email_data.selected_products):
            try:
                product: ProductDTO
                product_by_id = ProductModel.objects.get(pk=product.id)
                with open(product_by_id.image.path, "rb") as image_file:
                    mime_image = MIMEImage(image_file.read(), _subtype=product_by_id.image.name.split(".")[-1])
                    cid = f"product_image_{index}"
                    mime_image.add_header("Content-ID", f"<{cid}>")
                    mime_image.add_header("Content-Disposition", "inline", filename=product_by_id.image.name)
                    msg.attach(mime_image)
                    product.image_cid = cid
            except FileNotFoundError:
                logger.info(f"Image not found: {product_by_id.image.path}")

        # Renderiza el template a string
        html_content = render_to_string("components/consult_email.html", {"email_data": self.email_data})
        html_with_inline_styles = transform(html_content)
        msg.attach_alternative(html_with_inline_styles, "text/html")
        
        logger.info(f"Send inquiry email from {self.email_data.email}")
        msg.send()
        
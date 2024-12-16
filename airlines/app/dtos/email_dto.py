import json, logging
from dataclasses import dataclass, field
from typing import List, Optional, Any
from django.http import HttpRequest
from app.dtos.product_dto import ProductDTO

logger = logging.getLogger(__name__)


@dataclass
class EmailDataDTO:

    """
    Properies:
        owner_name: str
        email: str
        phone: str
        pet_name: str
        pet_age: Optional[int] = None
        pet_weight: Optional[float] = None
        pet_breed: Optional[str] = None
        pet_photo: Optional[Any] = None
        image_cid: Optional[str] = None
        travel_date: Optional[str] = None
        origin_city: Optional[str] = None
        destination_city: Optional[str] = None
        comments: Optional[str] = None
        selected_products: List[ProductDTO] = field(default_factory=list)
    """

    owner_name: str
    email: str
    phone: str
    pet_name: str
    pet_age: Optional[int] = None
    pet_weight: Optional[float] = None
    pet_breed: Optional[str] = None
    pet_photo: Optional[Any] = None
    image_cid: Optional[str] = None
    travel_date: Optional[str] = None
    origin_city: Optional[str] = None
    destination_city: Optional[str] = None
    comments: Optional[str] = None
    selected_products: List[ProductDTO] = field(default_factory=list)


    @classmethod
    def from_request(cls, request: HttpRequest) -> "EmailDataDTO":

        """
        Crea una instancia del DTO a partir de una solicitud HTTP.

        Args:
            request (HttpRequest): Request.

        Returns:
            EmailDataDTO: Instancia con los datos del email.
        """

        products_data = request.POST.getlist("selected_products", [])
        product_list: list[dict] = json.loads(products_data[0])
        products = []
        for product in product_list:
            try:
                product = ProductDTO(
                    id=product.get("id"),
                    name=product.get("name"),
                    price=float(product.get("price")),
                    quantity=int(product.get("quantity")),
                    stock=int(product.get("stock")),
                    total=float(product.get("total")),
                    image_url=product.get("image_url"),
                )
                products.append(product)
            except (ValueError, KeyError) as e:
                logger.error(f"Error al procesar producto: {e}")

        return cls(
            owner_name=request.POST.get("owner_name", "").strip(),
            email=request.POST.get("email", "").strip(),
            phone=request.POST.get("phone", "").strip(),
            pet_name=request.POST.get("pet_name", "").strip(),
            pet_age=request.POST.get("pet_age"),
            pet_weight=request.POST.get("pet_weight"),
            pet_breed=request.POST.get("pet_breed", "").strip(),
            pet_photo=request.FILES.get("pet_photo"),
            travel_date=request.POST.get("travel_date"),
            origin_city=request.POST.get("origin_city", "").strip(),
            destination_city=request.POST.get("destination_city", "").strip(),
            comments=request.POST.get("comments", "").strip(),
            selected_products=products,
        )
    
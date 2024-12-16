import logging
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class ProductDTO:

    """
    Properties:
        _instances: list[ProductDTO]
    """

    _instances = []

    def __init__(
            self,
            id: int,
            name: str,
            price: float,
            quantity: int,
            stock: int,
            total: float = None,
            image_url: Optional[str] = None,
            image_cid: Optional[str] = None
        ) -> None:

        """ Inicializador de ProductDTO. """

        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.stock = stock
        self.total = total
        self.image_url = image_url
        self.image_cid = image_cid
        self.__class__._instances.append(self)
        
    @property
    def to_dict(self) -> dict:

        """ Devuelve un diccionario con los datos de la instancia. """

        return self.__dict__

    # @classmethod
    # def get_by_id(cls, product_id: int) -> Optional["ProductDTO"] | None:

    #     """
    #     Busca y retorna una instancia de ProductoDto registrada en la clase por su ID.

    #     Args:
    #         product_id (int): ID de la instancia.

    #     Returns:
    #         ProductDTO | None: Instancia del objeto.
    #     """

    #     return next((dto for dto in cls._instances if dto.id == product_id), None)

    # @classmethod
    # def remove_instance(cls, product_id: int) -> Optional["ProductDTO"] | bool:
        
    #     """
    #     Elimina una instancia de ProductoDto de la lista _instances por su ID.

    #     Args:
    #         product_id (int): ID de la instancia.
        
    #     Returns:
    #         ProductDTO | bool: Retorna la instancia eliminada, de lo contrario `False`.
    #     """

    #     instance: "ProductDTO" = cls.get_by_id(product_id)
    #     if instance:
    #         instance = cls._instances.pop(instance)
    #         return instance
    #     return False
    
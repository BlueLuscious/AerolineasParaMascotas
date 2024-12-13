from django.db import models
from colorfield import fields


class PaletteModel(models.Model):

    """
    Palette Model.
    
    Fields:
        name (str): Palette name, reference.
        primary_colour (str): Hexadecimal colour (Ej. #FFFFFF).
        secondary_colour (str): Hexadecimal colour (Ej. #FFFFFF).
        terciary_colour (str): Hexadecimal colour (Ej. #FFFFFF).
    """

    name = fields.CharField(
        max_length=128,
        default=None,
        verbose_name="Nombre de la paleta",
        help_text="Nombre de referencia de la paleta",
    )
    primary_colour = fields.ColorField(
        default="#ffffff",
        verbose_name="Color Primario",
        help_text="Color para las tarjetas y/o fondos",
    )
    secondary_colour = fields.ColorField(
        default="#000000",
        verbose_name="Color Secundario",
        help_text="Color para los botones",
    )
    terciary_colour = fields.ColorField(
        default="#FFF000",
        verbose_name="Color Terciario",
        help_text="Color para las fuentes de texto",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "primary_colour", "secondary_colour", "terciary_colour", ],
                name="existing_palette"
            )
        ]

    def __str__(self) -> str:

        """ Sobreescritura del metodo __str__. """

        return self.name
    
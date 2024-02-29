from django.shortcuts import render
from django.views import View

class CategoryView(View):
    def get(self, request, boton_id):
        if boton_id == 1:
            return render(request, 'Razas.html')
        elif boton_id == 2:
            return render(request, 'Paises.html')
        elif boton_id == 3:
            return render(request, 'Viaja_tranquilo.html')
        elif boton_id == 4:
            return render(request, 'Requisitos.html')

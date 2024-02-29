from django.shortcuts import render
from django.views import View

class SubcategoryView(View):
    def get(self, request, boton_id):
        if boton_id == 1:
            return render(request, 'Requisitos.html')
        elif boton_id == 2:
            return render(request, 'Continents/Europa.html')
        elif boton_id == 3:
            return render(request, 'Continents/Inglaterra.html')
        elif boton_id == 4:
            return render(request, 'Requisitos.html')

from django_unicorn.components import UnicornView


class CartView(UnicornView):
    
    selected_products = []

    def add_product(self, id):
        pass
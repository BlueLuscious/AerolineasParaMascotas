import json
from django_unicorn.components import UnicornView
from store.models import ProductModel

class CartView(UnicornView):
    selected_products = []
    selected_products_string = ""
    total_gral = 0.0

    def add_product(self, instance: ProductModel):
        for product in self.selected_products:
            if product['id'] == instance.id:
                if product['quantity'] < product['stock']:
                    product['quantity'] += 1
                    product['total'] = product['quantity'] * float(product['price'])
                    self.calculate_total_gral()
                return

        if instance.stock > 0:
            self.selected_products.append({
                'id': instance.id,
                'name': instance.name,
                'price': float(instance.price),  
                'image_url': instance.image.url,
                'quantity': 1,
                'stock': instance.stock,
                'total': float(instance.price),  
            })
            self.selected_products_string = json.dumps(self.selected_products)
            self.calculate_total_gral()

    def remove_product(self, product_id):
        self.selected_products = [product for product in self.selected_products if product['id'] != product_id]
        self.selected_products_string = json.dumps(self.selected_products)
        self.calculate_total_gral()

    def update_quantity(self, product_id, quantity):
        try:
            quantity = int(quantity)
        except ValueError:
            return

        for product in self.selected_products:
            if product['id'] == product_id:
                if 1 <= quantity <= product['stock']:
                    product['quantity'] = quantity
                    product['total'] = product['quantity'] * float(product['price'])
                    self.calculate_total_gral()
                return

    def calculate_total_gral(self):
        self.total_gral = sum(float(product['total']) for product in self.selected_products)
        
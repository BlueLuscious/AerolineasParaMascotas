from django_unicorn.components import UnicornView
from store.models import ProductModel


class CartView(UnicornView):
    
    selected_products = []
    
    def add_product(self, instance:ProductModel):
        for product in self.selected_products:
            if product['id']== instance.id:
                product['quantity'] += 1
                return
        
        self.selected_products.append({
            'id': instance.id,
            'name': instance.name,
            'price':instance.price,
            'image_url': instance.image.url,
            'quantity':1,
        })

    def remove_product(self, product_id):
        self.selected_products = [product for product in self.selected_products if product['id'] != product_id]

    def update_quantity(self, product_id, quantity):
        try:
            quantity = int(quantity) 
        except ValueError:
            return

        for product in self.selected_products:
            if product['id'] == product_id:
                if 1 <= quantity <= product['stock']:
                    product['quantity'] = quantity
                return
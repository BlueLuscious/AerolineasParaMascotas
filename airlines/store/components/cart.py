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
            'quantity':1,
        })


from django_unicorn.components import UnicornView


class CartView(UnicornView):
    
    selected_products = []
    
    def add_product(self, id, name, price):
        for product in self.selected_products:
            if product['id']== id:
                product['quantity'] += 1
                return
        
        self.selected_products.append({
            'id': id,
            'name': name,
            'price':price,
            'quantity':1,
        })


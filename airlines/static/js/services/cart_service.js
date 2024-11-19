export class CartService{

    static addProduct(id,name,price){
        Unicorn.call('cart','add_product', id, name, price)
    }
}
export class CartService{

    static addProduct(id){
        Unicorn.call('cart','add_product', id)
    }
}
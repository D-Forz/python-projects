from product import Product

class Order:
    count_order = 0

    @classmethod
    def new_order(cls):
        cls.count_order += 1
        return cls.count_order

    def __init__(self, products):
        self._order_id = Order.new_order()
        self._products = list(products)
    
    @property
    def order_id(self):
        return self._order_id
    
    def add_product(self, product):
        self._products.append(product)
    
    def total_price(self):
        total = 0
        for product in self._products:
            total += product.price
        return total
    
    def __str__(self) -> str:
        products_str = ''
        for product in self._products:
            products_str += product.__str__() + ' | '
        return f"Order ID: {self._order_id}\nProducts: {products_str}"

if __name__ == '__main__':
    new_product0 = Product("Shoes", 100.00)
    new_product1 = Product("T-Shirt", 50.00)
    new_product2 = Product("Socks", 20.00)
    new_product4 = Product("Sneakers", 200.99)
    products0 = [new_product0, new_product1, new_product2]
    new_order = Order(products0)
    new_order.add_product(new_product4)
    print(new_order)
    print(f"Total: {new_order.total_price()}")
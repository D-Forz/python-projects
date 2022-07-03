class Product:
    count_product = 0

    @classmethod
    def new_product(cls):
        cls.count_product += 1
        return cls.count_product

    def __init__(self, name, price):
        self._product_id = Product.new_product()
        self._name = name
        self._price = price
    
    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    def __str__(self) -> str:
        return f"Id product: {self._product_id}, name: {self._name}, price: {self._price}"

if __name__ == '__main__':
    new_product0 = Product("Shoes", 100.00)
    print(new_product0)
    new_product1 = Product("T-Shirt", 50.00)
    print(new_product1)
class Order:
    def __init__(self, key: int, price: float):
        self.key = key
        self.price = price

    # vincula uma loja a um pedido
    def add_store(self, store):
        self.store = store

    def __str__(self):
        return 'Order: {} \t{}\tPrice: R${:3.2f}'.format(self.key, self.store, self.price)

from .Order import Order


class Deliveryman:
    def __init__(self, key, commission: float):
        self.key = key
        self.orders = []
        self.exclusive_stores = []
        # commission value in R$
        self.commission = commission
        self.total_received = 0

    # vincula um pedido a um motoby
    def add_order(self, order: Order):
        value = self.commission + (order.price * order.store.commission_extra / 100.0)
        self.total_received += value
        self.orders.append(order)

    # define a lista de lojas esclusivas de um motoboy
    def add_exclusive_store(self, store):
        self.exclusive_stores.append(store)

    # verifica se uma loja é exclusiva do motoboy (1 para sim, -1 para não e 0 é neutro. isso ajuda na ordenação pela loja)
    def check_exclusive_store(self, store):
        if not len(self.exclusive_stores):
            return 0
        for exclusive_store in self.exclusive_stores:
            if exclusive_store.key == store.key:
                return 1
        return -1

    # retorna numero total de pedidos entregues por um motoboy
    def get_total_order(self):
        return len(self.orders)

    # retorna total recebido por um motoboy
    def get_total_received(self):
        return self.total_received

    def __str__(self):
        return '\n\nDeliveryman: {}\nTotal Orders: {}\nTotal Received: R${:3.2f}\n{}'.format(self.key, self.get_total_order(),
                                                                                  self.get_total_received(), '\n'.join([str(x) for x in self.orders]))

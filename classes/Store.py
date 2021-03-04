from .Order import Order


# entidade Loja
class Store:
    def __init__(self, key, commission_extra: int):
        self.key = key
        # comissao extra em %
        self.commission_extra = commission_extra
        # lista de pedidos
        self.orders = []

        # associa um pedido a uma loja
    def create_order(self, order_: Order):
        order_.add_store(self)
        self.orders.append(order_)

    def __str__(self):
        return 'Store: {}'.format(self.key)

    # ordena e seleciona um motoby a um pedido
    def change_deliveryman(self, deliveryman_list_: list):

        # ordenação de acordo com a prioridade por exclusividade do motoboy
        deliveryman_list_.sort(key=lambda x: x.check_exclusive_store(self), reverse=True)

        # para cada pedido é selecionado o proximo motoboy válido para a entrega
        # (excluidos os motoboys exclusivos de outras lojas
        for order in self.orders:
            deliveryman = deliveryman_list_.pop(0)
            # se for maior que zero, um motoboy está apto a entregar por essa loja
            if deliveryman.check_exclusive_store(self) >= 0:
                deliveryman.add_order(order)
            deliveryman_list_.append(deliveryman)

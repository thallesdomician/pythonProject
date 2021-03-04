from classes.Deliveryman import Deliveryman
from classes.Order import Order
from classes.Store import Store
from classes.Finder import Finder

def options():
    print('\n\nSelect a Deliveryman:')
    print('ID(int) to show unique.')
    print('0 or blank to all.')
    print('-1 to exit.')

def run(deliveryman_list, store_list):
    deliveryman_ = Finder.deliveryman(deliveryman_list, 4)

    store = Finder.store(store_list, 1)
    deliveryman_.add_exclusive_store(store)
    store.create_order(Order(1, 50))
    store.create_order(Order(2, 50))
    store.create_order(Order(3, 50))

    store = Finder.store(store_list, 2)
    store.create_order(Order(1, 50))
    store.create_order(Order(2, 50))
    store.create_order(Order(3, 50))
    store.create_order(Order(4, 50))

    store = Finder.store(store_list, 3)
    store.create_order(Order(1, 50))
    store.create_order(Order(2, 50))
    store.create_order(Order(3, 100))

    for store in store_list:
        store.change_deliveryman(deliveryman_list)


if __name__ == '__main__':
    deliveryman_list = [
        Deliveryman(1, 2.0),
        Deliveryman(2, 2.0),
        Deliveryman(3, 2.0),
        Deliveryman(4, 2.0),
        Deliveryman(5, 3.0),
    ]

    store_list = [
        Store(1, 5.0),
        Store(2, 5.0),
        Store(3, 15.0),
    ]

    run(deliveryman_list, store_list)

    while True:
        options()
        value = int(input('>>> ') or 0)
        if value == -1:
            exit('exit')
        elif not value:
            for i in deliveryman_list:
                print(i)
        else:
            deliveryman = Finder.deliveryman(deliveryman_list,value)
            print(deliveryman)


from .Deliveryman import Deliveryman

from .Store import Store

class Finder:

    @staticmethod
    def store(list_store, key) -> Store:
        for store in list_store:
            if store.key == key:
                return store
        return None

    @staticmethod
    def deliveryman(list_deliveryman, key) -> Deliveryman:
        for deliveryman in list_deliveryman:
            if deliveryman.key == key:
                return deliveryman
        return None
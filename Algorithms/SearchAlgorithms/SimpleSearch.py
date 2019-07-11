# Простой поиск.
class SimpleSearch():

    def simple_search(self, collection, item):
        id = 0
        for target in collection:
            if target == item:
                return id
            id += 1
        return None

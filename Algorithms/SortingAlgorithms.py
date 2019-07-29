import random

class SortingAlgorithms():
    # Поиск наименьшего элемента.
    def find_smallest(self, collection):
        smallest = collection[0]
        smallest_index = 0
        for idx in range(1, len(collection)):
            if collection[idx] < smallest:
                smallest = collection[idx]
                smallest_index = idx
        return smallest_index

    # Алгоритм сортировки выбором.
    def selection_sort(self, collection):
        sort_collection = []
        for idx in range(len(collection)):
            smallest = self.find_smallest(collection)
            sort_collection.append(collection.pop(smallest))
        return sort_collection

    # Алгоритм быстрой сортировки.
    def quick_sort(self, collection):
        if len(collection) < 2: # Базовый случай.
            return collection
        else:                   # Рекурсивный случай.
            random_idx = random.randrange(0, len(collection))
            pivot = collection[random_idx] # Если всегда выбирать опорным элементом случайный элемент в массиве, 
                                           # бы­страя сортировка в среднем завершится за время О(п log п).
            less = [i for i in collection[1:] if i <= pivot]    # Подмассив элементов, меньше опорного.
            greater = [i for i in collection[1:] if i > pivot]  # Подмассив элементов, больших опорного.
            return self.quick_sort(less) + [pivot] + self.quick_sort(greater)
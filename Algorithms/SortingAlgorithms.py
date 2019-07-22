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
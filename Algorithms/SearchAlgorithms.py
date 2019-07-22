class SearchAlgorithms():
    # Алгоритм простого поиска.
    def simple_search(self, collection, item):
        id = 0
        for target in collection:
            if target == item:
                return id
            id += 1
        return None

    # Алгоритм бинарного поиска.
    def binary_search(self, collection, item):
        low = 0
        high = len(collection) - 1

        while low <= high:
            mid = (low + high)
            guess = collection[mid]
            if guess == item:
                return mid
            elif guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None


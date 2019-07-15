# Пример реализации бинарного поиска.
class BinarySearch():

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
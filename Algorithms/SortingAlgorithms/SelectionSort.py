# Алгоритм сортировки выбором.

class SelectionSort():

    def find_smallest(self, arr):
        smallest = arr[0]
        smallest_index = 0
        for idx in range(1, len(arr)):
            if arr[idx] < smallest:
                smallest = arr[idx]
                smallest_index = idx
        return smallest_index

    def selection_sort(self, arr):
        sortArr = []
        for idx in range(len(arr)):
            smallest = self.find_smallest(arr)
            sortArr.append(arr.pop(smallest))
        return sortArr

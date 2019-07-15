import unittest
import time
from Algorithms.SortingAlgorithms.SelectionSort import SelectionSort as ss

class SortingAlgorithmsTests(unittest.TestCase):

    def SelectionSortTest(self):
        # Arrage
        unsortedCollection = [5, 4, 1, 7, 44, 12, 65, 0]
        fakeSortedCollection = [0, 1, 4, 5, 7, 12, 44, 65]

        # Act
        sortedCollection = ss.selection_sort(ss, unsortedCollection)

        # Assert
        self.assertEqual(fakeSortedCollection, sortedCollection)


if __name__ == '__main__':
    unittest.main()

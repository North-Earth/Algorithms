import unittest
from Algorithms1.BinarySearch import BinarySearch as bs

class BinarySearchTest(unittest.TestCase):

    def test_serch(self):
        # Arrage
        collection = [1, 3, 5, 7, 9, 11]
        trueItem = 9
        noneItem = -99
        fakeTrueResult = 4
        fakeNoneResult = None

        # Act
        trueResult = bs.binary_search(self,collection, trueItem)
        noneResult = bs.binary_search(self,collection, noneItem)

        # Assert
        self.assertEqual(fakeTrueResult, trueResult)
        self.assertEqual(fakeNoneResult, noneResult)

if __name__ == '__main__':
    unittest.main()
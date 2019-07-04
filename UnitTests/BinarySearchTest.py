import unittest
from Algorithms.BinarySearch import BinarySearch as bs

# ~py -m UnitTests.BinarySearchTest

class BinarySearchTest(unittest.TestCase):

    def test_serch(self):
        # Arrage
        collection = range(0,10000,2)
        trueItem = 450
        fakeTrueResult = 225

        noneItem = -99
        fakeNoneResult = None

        falseItem = 0
        fakeFalseResult = 1

        # Act
        trueResult = bs.binary_search(self,collection, trueItem)
        noneResult = bs.binary_search(self,collection, noneItem)

        # Assert
        self.assertEqual(fakeTrueResult, trueResult)
        self.assertEqual(fakeNoneResult, noneResult)
        self.assertFalse(fakeFalseResult, falseItem)

if __name__ == '__main__':
    unittest.main()
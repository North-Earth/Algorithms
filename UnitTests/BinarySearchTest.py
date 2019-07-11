import unittest
import time
from Algorithms.BinarySearch import BinarySearch as bs
from Algorithms.SimpleSearch import SimpleSearch as ss

# ~py -m UnitTests.BinarySearchTest


class BinarySearchTest(unittest.TestCase):

    def test_serch(self):
        # Arrage
        collection = range(0, 10000, 2)
        trueItem = 450
        fakeTrueResult = 225

        noneItem = -99
        fakeNoneResult = None

        falseItem = 0
        fakeFalseResult = 1

        # Act
        trueResult = bs.binary_search(self, collection, trueItem)
        noneResult = bs.binary_search(self, collection, noneItem)
        falseResult = bs.binary_search(self, collection, falseItem)

        # Assert
        self.assertEqual(fakeTrueResult, trueResult)
        self.assertEqual(fakeNoneResult, noneResult)
        self.assertNotEqual(fakeFalseResult, falseResult)

    def test_serch_time(self):
        # Arrage
        collection = range(0, 10000000, 1)
        item = 8937532

        # Act
        start_time = time.time()
        binaryResult = bs.binary_search(self, collection, item)
        print("\nbinary: %s seconds" % (time.time() - start_time))

        start_time = time.time()
        simpleResult = ss.simple_search(self, collection, item)
        print("simple: %s seconds" % (time.time() - start_time))

        # Assert
        self.assertEqual(binaryResult, simpleResult)

if __name__ == '__main__':
    unittest.main()
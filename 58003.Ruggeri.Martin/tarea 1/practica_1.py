import unittest
from sorting import Sort


class BubbleSortTest(unittest.TestCase):
    def testArr1(self):
        arr1 = [36, 71, 16, 21, 73, 9, 0, 40, 66, 7]
        bubble1 = Sort().BubbleSort(arr1)
        self.assertEqual(bubble1, [0, 7, 9, 16, 21, 36, 40, 66, 71, 73])

    def testArr2(self):
        arr2 = [0, 2, 23, 4, 2, 8, 1, 25, 6, 9]
        bubble2 = Sort().BubbleSort(arr2)
        self.assertEqual(bubble2, [0, 1, 2, 2, 4, 6, 8, 9, 23, 25])

    def testArr3(self):
        arr3 = [5, 0, 15, 25, 21, 35, 40, 25, 6, 9]
        bubble3 = Sort().BubbleSort(arr3)
        self.assertEqual(bubble3, [0, 5, 6, 9, 15, 21, 25, 25, 35, 40])


if __name__ == '__main__':
    unittest.main()

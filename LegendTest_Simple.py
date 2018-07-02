import unittest
from Legend import *

class LegendTest(unittest.TestCase):

    def test_is_princess(self):
        legend = Legend()
        self.assertEqual(True,  legend.is_princess('Zelda'))
        self.assertEqual(True,  legend.is_princess('Seek'))
        self.assertEqual(False, legend.is_princess('Saria'))
        self.assertEqual(True,  legend.is_princess('Ruto'))
        self.assertEqual(False, legend.is_princess('Malon'))

if __name__ == "__main__":
    unittest.main()

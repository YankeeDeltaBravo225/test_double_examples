import unittest
from unittest.mock import Mock

from Legend import *

#
# Usage of built-in Mocks
#
class LegendTest(unittest.TestCase):

    def test_set_cv_mock(self):
        mock = Mock(return_value='Link')

        legend = Legend()
        legend.navi.ask = mock
        legend.set_cv()

        self.assertEqual(100,       legend.cv_volume)
        self.assertEqual('Hiyama', legend.cv_actor)
        self.assertEqual(1,         mock.call_count)


if __name__ == "__main__":
    unittest.main()

import unittest
import inspect
from Legend import *

class LegendTest(unittest.TestCase):

    # Test stub
    def naviAskStub(self, message):
        return self.navi_ask_resp

    # Usage of test spy
    def test_set_cv_stub(self):
        legend = Legend()

        self.navi_ask_resp = 'Link'
        legend.navi.ask = self.naviAskStub

        legend.set_cv()

        self.assertEqual(100,       legend.cv_volume)
        self.assertEqual('Hiyama', legend.cv_actor)


    # Test spy
    def naviAskSpy(self, message):
        self.navi_ask_cnt += 1
        return self.navi_ask_resp


    # Usage of test spy
    def test_set_cv_spy(self):
        legend = Legend()

        self.navi_ask_resp = 'Link'
        self.navi_ask_cnt = 0
        legend.navi.ask = self.naviAskSpy

        legend.set_cv()

        self.assertEqual(100,       legend.cv_volume)
        self.assertEqual('Hiyama', legend.cv_actor)
        self.assertEqual(1,         self.navi_ask_cnt)


    # Test mock
    def naviAskMock(self, message):
        self.navi_ask_cnt += 1
        self.assertTrue(message.startswith('Hey'))
        return self.navi_ask_resp


    # Usage of test mock
    def test_set_cv_mock(self):
        legend = Legend()

        self.navi_ask_resp = 'Link'
        self.navi_ask_cnt = 0
        legend.navi.ask = self.naviAskMock

        legend.set_cv()

        self.assertEqual(100,       legend.cv_volume)
        self.assertEqual('Hiyama', legend.cv_actor)
        self.assertEqual(1,         self.navi_ask_cnt)




if __name__ == "__main__":
    unittest.main()

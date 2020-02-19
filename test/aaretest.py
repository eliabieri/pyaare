import unittest
from unittest import mock
import json
import os
from pyaare.pyaare import PyAare

class AareTest(unittest.TestCase):

    def getData(self):
        with open(os.path.join("test", "test.json")) as f:
            return json.load(f)

    @mock.patch.object(PyAare, "_getData", getData)
    def testHappyDay(self):
        aare = PyAare("Bern")
        self.assertAlmostEqual(6.1, aare.tempC)
        self.assertEqual("Gschider Iglu boue… aber mit was?", aare.tempText)
        self.assertEqual(87, aare.flow)
        self.assertEqual("nid viu", aare.flowText)

    def testCityNotSupperted(self):
        with self.assertRaises(RuntimeError):
            aare = PyAare("unsupportedCity")

if __name__ == '__main__':
    unittest.main()